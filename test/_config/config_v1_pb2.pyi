from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Batch(_message.Message):
    __slots__ = ["common", "context", "events"]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    common: BatchCommon
    context: Context
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, common: _Optional[_Union[BatchCommon, _Mapping]] = ..., context: _Optional[_Union[Context, _Mapping]] = ..., events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

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

class Context(_message.Message):
    __slots__ = ["application", "appsflyer", "device", "identify", "os", "user"]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPSFLYER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    application: ContextApplication
    appsflyer: ContextAppsflyer
    device: ContextDevice
    identify: ContextIdentify
    os: ContextOs
    user: ContextUser
    def __init__(self, application: _Optional[_Union[ContextApplication, _Mapping]] = ..., device: _Optional[_Union[ContextDevice, _Mapping]] = ..., identify: _Optional[_Union[ContextIdentify, _Mapping]] = ..., os: _Optional[_Union[ContextOs, _Mapping]] = ..., appsflyer: _Optional[_Union[ContextAppsflyer, _Mapping]] = ..., user: _Optional[_Union[ContextUser, _Mapping]] = ...) -> None: ...

class ContextApplication(_message.Message):
    __slots__ = ["app_id", "app_platform", "app_version"]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_platform: str
    app_version: str
    def __init__(self, app_id: _Optional[str] = ..., app_version: _Optional[str] = ..., app_platform: _Optional[str] = ...) -> None: ...

class ContextAppsflyer(_message.Message):
    __slots__ = ["appsflyer_id", "appsflyer_media_source"]
    APPSFLYER_ID_FIELD_NUMBER: _ClassVar[int]
    APPSFLYER_MEDIA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    appsflyer_id: str
    appsflyer_media_source: str
    def __init__(self, appsflyer_id: _Optional[str] = ..., appsflyer_media_source: _Optional[str] = ...) -> None: ...

class ContextDevice(_message.Message):
    __slots__ = ["device_brand", "device_carrier", "device_model"]
    DEVICE_BRAND_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CARRIER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    device_brand: str
    device_carrier: str
    device_model: str
    def __init__(self, device_brand: _Optional[str] = ..., device_model: _Optional[str] = ..., device_carrier: _Optional[str] = ...) -> None: ...

class ContextIdentify(_message.Message):
    __slots__ = ["gaid", "idfa", "idfv"]
    GAID_FIELD_NUMBER: _ClassVar[int]
    IDFA_FIELD_NUMBER: _ClassVar[int]
    IDFV_FIELD_NUMBER: _ClassVar[int]
    gaid: str
    idfa: str
    idfv: str
    def __init__(self, idfa: _Optional[str] = ..., idfv: _Optional[str] = ..., gaid: _Optional[str] = ...) -> None: ...

class ContextOs(_message.Message):
    __slots__ = ["os_name", "os_version"]
    OS_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    os_name: str
    os_version: str
    def __init__(self, os_name: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...

class ContextUser(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ["common", "header", "payload"]
    COMMON_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    common: EventCommon
    header: EventHeader
    payload: EventPayload
    def __init__(self, common: _Optional[_Union[EventCommon, _Mapping]] = ..., header: _Optional[_Union[EventHeader, _Mapping]] = ..., payload: _Optional[_Union[EventPayload, _Mapping]] = ...) -> None: ...

class EventCommon(_message.Message):
    __slots__ = ["event_ts", "event_type", "session_event_seq_num", "session_id"]
    EVENT_TS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SESSION_EVENT_SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    event_ts: int
    event_type: int
    session_event_seq_num: int
    session_id: int
    def __init__(self, event_type: _Optional[int] = ..., event_ts: _Optional[int] = ..., session_id: _Optional[int] = ..., session_event_seq_num: _Optional[int] = ...) -> None: ...

class EventHeader(_message.Message):
    __slots__ = ["parent"]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: EventHeaderParent
    def __init__(self, parent: _Optional[_Union[EventHeaderParent, _Mapping]] = ...) -> None: ...

class EventHeaderParent(_message.Message):
    __slots__ = ["parent_elements"]
    PARENT_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent_elements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent_elements: _Optional[_Iterable[str]] = ...) -> None: ...

class EventPayload(_message.Message):
    __slots__ = ["event_1", "event_2", "event_3", "event_4", "event_5", "event_6"]
    EVENT_1_FIELD_NUMBER: _ClassVar[int]
    EVENT_2_FIELD_NUMBER: _ClassVar[int]
    EVENT_3_FIELD_NUMBER: _ClassVar[int]
    EVENT_4_FIELD_NUMBER: _ClassVar[int]
    EVENT_5_FIELD_NUMBER: _ClassVar[int]
    EVENT_6_FIELD_NUMBER: _ClassVar[int]
    event_1: EventPayloadSessionStart
    event_2: EventPayloadOnboardingStart
    event_3: EventPayloadOnboardingFinish
    event_4: EventPayloadPageOpen
    event_5: EventPayloadPermissionsRequest
    event_6: EventPayloadEdgeCase
    def __init__(self, event_1: _Optional[_Union[EventPayloadSessionStart, _Mapping]] = ..., event_2: _Optional[_Union[EventPayloadOnboardingStart, _Mapping]] = ..., event_3: _Optional[_Union[EventPayloadOnboardingFinish, _Mapping]] = ..., event_4: _Optional[_Union[EventPayloadPageOpen, _Mapping]] = ..., event_5: _Optional[_Union[EventPayloadPermissionsRequest, _Mapping]] = ..., event_6: _Optional[_Union[EventPayloadEdgeCase, _Mapping]] = ...) -> None: ...

class EventPayloadEdgeCase(_message.Message):
    __slots__ = ["prop_boolean", "prop_boolean_array", "prop_boolean_map", "prop_decimal_1", "prop_decimal_2", "prop_decimal_array", "prop_decimal_map", "prop_enum", "prop_enum_array", "prop_enum_map", "prop_integer", "prop_integer_array", "prop_integer_map", "prop_string", "prop_string_array", "prop_string_map", "prop_timestamp", "prop_timestamp_array", "prop_timestamp_map"]
    PROP_BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    PROP_BOOLEAN_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_1_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_2_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_ENUM_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_ENUM_FIELD_NUMBER: _ClassVar[int]
    PROP_ENUM_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_STRING_FIELD_NUMBER: _ClassVar[int]
    PROP_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_TIMESTAMP_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROP_TIMESTAMP_MAP_FIELD_NUMBER: _ClassVar[int]
    prop_boolean: bool
    prop_boolean_array: _containers.RepeatedScalarFieldContainer[bool]
    prop_boolean_map: bool
    prop_decimal_1: str
    prop_decimal_2: str
    prop_decimal_array: _containers.RepeatedScalarFieldContainer[str]
    prop_decimal_map: str
    prop_enum: int
    prop_enum_array: _containers.RepeatedScalarFieldContainer[int]
    prop_enum_map: int
    prop_integer: int
    prop_integer_array: _containers.RepeatedScalarFieldContainer[int]
    prop_integer_map: int
    prop_string: str
    prop_string_array: _containers.RepeatedScalarFieldContainer[str]
    prop_string_map: str
    prop_timestamp: int
    prop_timestamp_array: _containers.RepeatedScalarFieldContainer[int]
    prop_timestamp_map: int
    def __init__(self, prop_boolean: bool = ..., prop_decimal_1: _Optional[str] = ..., prop_decimal_2: _Optional[str] = ..., prop_enum: _Optional[int] = ..., prop_integer: _Optional[int] = ..., prop_string: _Optional[str] = ..., prop_timestamp: _Optional[int] = ..., prop_boolean_array: _Optional[_Iterable[bool]] = ..., prop_decimal_array: _Optional[_Iterable[str]] = ..., prop_enum_array: _Optional[_Iterable[int]] = ..., prop_integer_array: _Optional[_Iterable[int]] = ..., prop_string_array: _Optional[_Iterable[str]] = ..., prop_timestamp_array: _Optional[_Iterable[int]] = ..., prop_boolean_map: bool = ..., prop_decimal_map: _Optional[str] = ..., prop_enum_map: _Optional[int] = ..., prop_integer_map: _Optional[int] = ..., prop_string_map: _Optional[str] = ..., prop_timestamp_map: _Optional[int] = ...) -> None: ...

class EventPayloadOnboardingFinish(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventPayloadOnboardingStart(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventPayloadPageOpen(_message.Message):
    __slots__ = ["page_id"]
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    page_id: str
    def __init__(self, page_id: _Optional[str] = ...) -> None: ...

class EventPayloadPermissionsRequest(_message.Message):
    __slots__ = ["is_granted", "type"]
    IS_GRANTED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    is_granted: bool
    type: str
    def __init__(self, is_granted: bool = ..., type: _Optional[str] = ...) -> None: ...

class EventPayloadSessionStart(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
