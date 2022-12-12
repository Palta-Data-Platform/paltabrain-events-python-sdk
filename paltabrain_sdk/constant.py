ENDPOINT_BATCH_PROTO = '/v2/paltabrain'

SDK_NAME = 'Paltabrain Python SDK'
CONTENT_TYPE = 'application/protobuf'

REQUEST_TIMEOUT = 10                    # 10s timeout per request
REQUEST_MAX_WORKERS = 20                # up to 20 requests can be sent in parallel

DEFAULT_FLUSH_BUFFER_SIZE = 100         # 100 events
DEFAULT_FLUSH_INTERVAL_MS = 5000        # 5s interval
DEFAULT_FLUSH_MAX_RETRIES = 5           # 5 retries before giving up

BATCH_MAX_BYTE_SIZE = 512 * 1024        # 512Kb

CONTROL_THREAD_LOOP_INTERVAL = 0.05     # 50ms sleep between cycles
