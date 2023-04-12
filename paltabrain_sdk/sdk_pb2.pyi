from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Batch(_message.Message):
    __slots__ = ["common", "context", "events", "telemetry"]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    common: BatchCommon
    context: bytes
    events: _containers.RepeatedCompositeFieldContainer[Event]
    telemetry: BatchTelemetry
    def __init__(self, common: _Optional[_Union[BatchCommon, _Mapping]] = ..., context: _Optional[bytes] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., telemetry: _Optional[_Union[BatchTelemetry, _Mapping]] = ...) -> None: ...

class BatchCommon(_message.Message):
    __slots__ = ["batch_id", "country_code", "instance_id", "locale", "utc_offset"]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    UTC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    country_code: str
    instance_id: str
    locale: str
    utc_offset: int
    def __init__(self, instance_id: _Optional[str] = ..., batch_id: _Optional[str] = ..., country_code: _Optional[str] = ..., locale: _Optional[str] = ..., utc_offset: _Optional[int] = ...) -> None: ...

class BatchTelemetry(_message.Message):
    __slots__ = ["events_dropped", "events_reporting_speed", "prev_connection_speed", "prev_request_time", "serialization_errors", "storage_errors", "storage_used", "time_since_last_batch", "trigger_type"]
    EVENTS_DROPPED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_REPORTING_SPEED_FIELD_NUMBER: _ClassVar[int]
    PREV_CONNECTION_SPEED_FIELD_NUMBER: _ClassVar[int]
    PREV_REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_USED_FIELD_NUMBER: _ClassVar[int]
    TIME_SINCE_LAST_BATCH_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    events_dropped: int
    events_reporting_speed: str
    prev_connection_speed: str
    prev_request_time: int
    serialization_errors: _containers.RepeatedScalarFieldContainer[str]
    storage_errors: _containers.RepeatedScalarFieldContainer[str]
    storage_used: str
    time_since_last_batch: int
    trigger_type: str
    def __init__(self, events_dropped: _Optional[int] = ..., prev_connection_speed: _Optional[str] = ..., prev_request_time: _Optional[int] = ..., events_reporting_speed: _Optional[str] = ..., serialization_errors: _Optional[_Iterable[str]] = ..., storage_errors: _Optional[_Iterable[str]] = ..., storage_used: _Optional[str] = ..., trigger_type: _Optional[str] = ..., time_since_last_batch: _Optional[int] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["common", "header", "payload"]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    common: EventCommon
    header: bytes
    payload: bytes
    def __init__(self, common: _Optional[_Union[EventCommon, _Mapping]] = ..., header: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class EventCommon(_message.Message):
    __slots__ = ["event_ts", "session_event_seq_num", "session_id"]
    EVENT_TS_FIELD_NUMBER: _ClassVar[int]
    SESSION_EVENT_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    event_ts: int
    session_event_seq_num: int
    session_id: int
    def __init__(self, event_ts: _Optional[int] = ..., session_id: _Optional[int] = ..., session_event_seq_num: _Optional[int] = ...) -> None: ...
