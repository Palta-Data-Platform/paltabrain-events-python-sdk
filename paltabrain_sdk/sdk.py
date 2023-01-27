from collections import deque
from concurrent.futures import ThreadPoolExecutor, Future
from logging import getLogger, NullHandler, DEBUG
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep
from threading import Lock, Thread
from typing import Dict, Generic, Optional, Tuple, TypeVar

from .constant import *
from .base import BaseContext, BaseEvent
from .sdk_pb2 import Batch as BatchMessage, Event as EventMessage
from .utils import time_ms, uuid_v7
from .version import __version__


logger = getLogger(__name__)
logger.addHandler(NullHandler())


C = TypeVar('C', bound=BaseContext)


class PaltabrainSdk(Generic[C]):
    BATCH_STATUS_SUCCESS = "SUCCESS"
    BATCH_STATUS_REJECT = "REJECT"
    BATCH_STATUS_EXCEPTION = "EXCEPTION"

    def __init__(self
                 , hostname: str
                 , api_key: str
                 , context: C
                 , instance_id: Optional[str] = None
                 , session_id: Optional[int] = None
                 , start_session: bool = False
                 , flush_buffer_size: int = DEFAULT_FLUSH_BUFFER_SIZE
                 , flush_interval_ms: int = DEFAULT_FLUSH_INTERVAL_MS
                 , flush_max_retries: int = DEFAULT_FLUSH_MAX_RETRIES
                 ):

        self.logger = logger

        self.hostname = hostname
        self.api_key = api_key

        self.context = context

        self.instance_id = instance_id if instance_id else uuid_v7(time_ms())
        self.session_id = session_id if session_id else (time_ms() if start_session else None)
        self.session_event_seq_num = 0

        self.flush_buffer_size = flush_buffer_size
        self.flush_interval_ms = flush_interval_ms
        self.flush_max_retries = flush_max_retries

        self.last_flush_ms = time_ms()
        self.last_exception: Optional[Exception] = None

        self.executor = ThreadPoolExecutor(max_workers=REQUEST_MAX_WORKERS)
        self.running_requests: Dict[str, Future] = {}

        self.event_buffer: deque[Tuple[bytes, EventMessage]] = deque()

        self.flush_lock = Lock()
        self.seq_num_lock = Lock()

        self.is_shutdown = False

        self.batch_counters = {
            self.BATCH_STATUS_SUCCESS: 0,
            self.BATCH_STATUS_REJECT: 0,
            self.BATCH_STATUS_EXCEPTION: 0,
        }

        self.http_adapter = HTTPAdapter(
            max_retries=Retry(
                total=self.flush_max_retries,
                status_forcelist=[429, 500, 502, 503, 504],
                method_whitelist=['GET', 'POST'],
                backoff_factor=0.1,
            )
        )

        self.control_thread = Thread(target=self._control_thread_loop)
        self.control_thread.start()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()

    def track(self, event: BaseEvent, context: Optional[C] = None):
        if not context:
            context = self.context

        context_bytes = context.serialize_context()
        event_message = self._build_event_message(event)

        self.event_buffer.append((context_bytes, event_message))

    def flush(self):
        with self.flush_lock:
            # If no events to send, exit immediately
            if len(self.event_buffer) == 0:
                self.last_flush_ms = time_ms()
                return

            # Create first batch with context and one event
            context_bytes, event_message = self.event_buffer.popleft()
            batch = self._build_batch_message(context_bytes, event_message)

            # As long as more events are available, keep iterating
            while len(self.event_buffer) > 0:
                context_bytes, event_message = self.event_buffer.popleft()

                if batch.context == context_bytes and (batch.ByteSize() + event_message.ByteSize()) <= BATCH_MAX_BYTE_SIZE:
                    # If context is the same, and next event will not exceed allowed bytes size, add event to current batch
                    batch.events.append(event_message)
                else:
                    # Otherwise, send currently accumulated batch and start a new batch
                    self._send_batch(batch)
                    batch = self._build_batch_message(context_bytes, event_message)

            # Send last accumulated batch after iteration
            self._send_batch(batch)
            self.last_flush_ms = time_ms()

    def shutdown(self):
        self.is_shutdown = True

        self.flush()
        self.executor.shutdown()
        self.control_thread.join()

    def _control_thread_loop(self):
        while True:
            self._control_thread_check_requests()

            if self.is_shutdown and len(self.running_requests) == 0:
                return
            else:
                self._control_thread_flush()

            sleep(CONTROL_THREAD_LOOP_INTERVAL)

    def _control_thread_check_requests(self):
        # Copy is required to prevent "dictionary changed size during iteration"
        for batch_id, f in self.running_requests.copy().items():
            if f.running():
                continue

            try:
                response = f.result()
            except Exception as e:
                self.last_exception = e

                self.batch_counters[self.BATCH_STATUS_EXCEPTION] += 1
                self.logger.warning(f"Batch: {batch_id}, Status: {self.BATCH_STATUS_EXCEPTION}, Reason: {str(e)}")
            else:
                if response.status_code == 200:
                    self.batch_counters[self.BATCH_STATUS_SUCCESS] += 1
                    self.logger.info(f"Batch {batch_id}, Status: {self.BATCH_STATUS_SUCCESS}, Time: {response.elapsed.total_seconds()}")
                else:
                    self.batch_counters[self.BATCH_STATUS_REJECT] += 1
                    self.logger.info(f"Batch {batch_id}, Status: {self.BATCH_STATUS_REJECT}, Code: {response.status_code}")

            del self.running_requests[batch_id]

    def _control_thread_flush(self):
        if len(self.event_buffer) >= self.flush_buffer_size or (time_ms() - self.last_flush_ms) >= self.flush_interval_ms:
            self.flush()

    def _send_batch(self, batch):
        session = Session()
        session.mount('https://', self.http_adapter)

        url = f"https://{self.hostname}{ENDPOINT_BATCH_PROTO}"

        headers = {
            'Content-Type': CONTENT_TYPE,
            'X-API-Key': self.api_key,
            'X-SDK-Name': SDK_NAME,
            'X-SDK-Version': __version__,
            'X-SDK-Client-Upload-TS': str(time_ms()),
        }

        data = batch.SerializeToString()

        if self.logger.isEnabledFor(DEBUG):
            self.logger.debug(str(batch))

        self.running_requests[batch.common.batch_id] = self.executor.submit(session.post, url, headers=headers, data=data, timeout=REQUEST_TIMEOUT)

    def _build_event_message(self, event: BaseEvent):
        event_message = EventMessage()

        event_message.common.event_ts = time_ms()

        if self.session_id:
            event_message.common.session_id = self.session_id

            with self.seq_num_lock:
                self.session_event_seq_num += 1
                event_message.common.session_event_seq_num = self.session_event_seq_num

        event_message.header = event.serialize_header()
        event_message.payload = event.serialize_payload()

        return event_message

    def _build_batch_message(self, context_bytes: bytes, first_event_message: EventMessage):
        batch_message = BatchMessage()

        batch_message.common.instance_id = self.instance_id
        batch_message.common.batch_id = uuid_v7(time_ms())

        batch_message.context = context_bytes
        batch_message.events.append(first_event_message)

        return batch_message
