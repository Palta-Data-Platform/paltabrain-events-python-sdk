from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class EventHeader(_message.Message):
    __slots__ = ["edge_case", "onboarding", "parent"]
    EDGE_CASE_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    edge_case: EventHeaderEdgeCase
    onboarding: EventHeaderOnboarding
    parent: EventHeaderParent
    def __init__(self, parent: _Optional[_Union[EventHeaderParent, _Mapping]] = ..., onboarding: _Optional[_Union[EventHeaderOnboarding, _Mapping]] = ..., edge_case: _Optional[_Union[EventHeaderEdgeCase, _Mapping]] = ...) -> None: ...

class EventHeaderEdgeCase(_message.Message):
    __slots__ = ["prop_boolean", "prop_decimal_1", "prop_decimal_2", "prop_enum", "prop_integer", "prop_integer_array", "prop_integer_map", "prop_string", "prop_timestamp"]
    class PropIntegerMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PROP_BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_1_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_2_FIELD_NUMBER: _ClassVar[int]
    PROP_ENUM_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_FIELD_NUMBER: _ClassVar[int]
    PROP_INTEGER_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_STRING_FIELD_NUMBER: _ClassVar[int]
    PROP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    prop_boolean: bool
    prop_decimal_1: str
    prop_decimal_2: str
    prop_enum: int
    prop_integer: int
    prop_integer_array: _containers.RepeatedScalarFieldContainer[int]
    prop_integer_map: _containers.ScalarMap[str, int]
    prop_string: str
    prop_timestamp: int
    def __init__(self, prop_boolean: bool = ..., prop_decimal_1: _Optional[str] = ..., prop_decimal_2: _Optional[str] = ..., prop_enum: _Optional[int] = ..., prop_integer: _Optional[int] = ..., prop_string: _Optional[str] = ..., prop_timestamp: _Optional[int] = ..., prop_integer_array: _Optional[_Iterable[int]] = ..., prop_integer_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EventHeaderOnboarding(_message.Message):
    __slots__ = ["onboarding_id", "onboarding_version"]
    ONBOARDING_ID_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_VERSION_FIELD_NUMBER: _ClassVar[int]
    onboarding_id: int
    onboarding_version: str
    def __init__(self, onboarding_id: _Optional[int] = ..., onboarding_version: _Optional[str] = ...) -> None: ...

class EventHeaderParent(_message.Message):
    __slots__ = ["parent_elements"]
    PARENT_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    parent_elements: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent_elements: _Optional[_Iterable[str]] = ...) -> None: ...

class EventPayload(_message.Message):
    __slots__ = ["event_1", "event_10", "event_11", "event_12", "event_13", "event_14", "event_15", "event_16", "event_17", "event_18", "event_19", "event_2", "event_20", "event_21", "event_22", "event_23", "event_24", "event_25", "event_26", "event_27", "event_28", "event_29", "event_3", "event_30", "event_31", "event_32", "event_33", "event_34", "event_4", "event_5", "event_6", "event_7", "event_8", "event_9"]
    EVENT_10_FIELD_NUMBER: _ClassVar[int]
    EVENT_11_FIELD_NUMBER: _ClassVar[int]
    EVENT_12_FIELD_NUMBER: _ClassVar[int]
    EVENT_13_FIELD_NUMBER: _ClassVar[int]
    EVENT_14_FIELD_NUMBER: _ClassVar[int]
    EVENT_15_FIELD_NUMBER: _ClassVar[int]
    EVENT_16_FIELD_NUMBER: _ClassVar[int]
    EVENT_17_FIELD_NUMBER: _ClassVar[int]
    EVENT_18_FIELD_NUMBER: _ClassVar[int]
    EVENT_19_FIELD_NUMBER: _ClassVar[int]
    EVENT_1_FIELD_NUMBER: _ClassVar[int]
    EVENT_20_FIELD_NUMBER: _ClassVar[int]
    EVENT_21_FIELD_NUMBER: _ClassVar[int]
    EVENT_22_FIELD_NUMBER: _ClassVar[int]
    EVENT_23_FIELD_NUMBER: _ClassVar[int]
    EVENT_24_FIELD_NUMBER: _ClassVar[int]
    EVENT_25_FIELD_NUMBER: _ClassVar[int]
    EVENT_26_FIELD_NUMBER: _ClassVar[int]
    EVENT_27_FIELD_NUMBER: _ClassVar[int]
    EVENT_28_FIELD_NUMBER: _ClassVar[int]
    EVENT_29_FIELD_NUMBER: _ClassVar[int]
    EVENT_2_FIELD_NUMBER: _ClassVar[int]
    EVENT_30_FIELD_NUMBER: _ClassVar[int]
    EVENT_31_FIELD_NUMBER: _ClassVar[int]
    EVENT_32_FIELD_NUMBER: _ClassVar[int]
    EVENT_33_FIELD_NUMBER: _ClassVar[int]
    EVENT_34_FIELD_NUMBER: _ClassVar[int]
    EVENT_3_FIELD_NUMBER: _ClassVar[int]
    EVENT_4_FIELD_NUMBER: _ClassVar[int]
    EVENT_5_FIELD_NUMBER: _ClassVar[int]
    EVENT_6_FIELD_NUMBER: _ClassVar[int]
    EVENT_7_FIELD_NUMBER: _ClassVar[int]
    EVENT_8_FIELD_NUMBER: _ClassVar[int]
    EVENT_9_FIELD_NUMBER: _ClassVar[int]
    event_1: EventPayloadSessionStart
    event_10: EventPayloadStrParamEvent
    event_11: EventPayloadBoolParamEvent
    event_12: EventPayloadIntParamEvent
    event_13: EventPayloadTimestampParamEvent
    event_14: EventPayloadDecimalParamEvent
    event_15: EventPayloadEnumParamEvent
    event_16: EventPayloadBoolListEvent
    event_17: EventPayloadDecimalListEvent
    event_18: EventPayloadEnumListEvent
    event_19: EventPayloadIntListEvent
    event_2: EventPayloadOnboardingStart
    event_20: EventPayloadStrListEvent
    event_21: EventPayloadTimestampListEvent
    event_22: EventPayloadBoolMapEvent
    event_23: EventPayloadDecimalMapEvent
    event_24: EventPayloadEnumMapEvent
    event_25: EventPayloadIntMapEvent
    event_26: EventPayloadStrMapEvent
    event_27: EventPayloadTimestampMapEvent
    event_28: EventPayloadDeprecatedEvent
    event_29: EventPayloadDeprecatedPropertyEvent
    event_3: EventPayloadOnboardingFinish
    event_30: EventPayloadKotlinKeywordEvent
    event_31: EventPayloadJavascriptKeywordEvent
    event_32: EventPayloadSwiftKeywordEvent
    event_33: EventPayloadPythonKeywordEvent
    event_34: EventPayloadIosOnlyEvent
    event_4: EventPayloadPageOpen
    event_5: EventPayloadPermissionsRequest
    event_6: EventPayloadEdgeCase
    event_7: EventPayloadBrandNewEvent
    event_8: EventPayloadTestCase
    event_9: EventPayloadEmptyParamEvent
    def __init__(self, event_1: _Optional[_Union[EventPayloadSessionStart, _Mapping]] = ..., event_2: _Optional[_Union[EventPayloadOnboardingStart, _Mapping]] = ..., event_3: _Optional[_Union[EventPayloadOnboardingFinish, _Mapping]] = ..., event_4: _Optional[_Union[EventPayloadPageOpen, _Mapping]] = ..., event_5: _Optional[_Union[EventPayloadPermissionsRequest, _Mapping]] = ..., event_6: _Optional[_Union[EventPayloadEdgeCase, _Mapping]] = ..., event_7: _Optional[_Union[EventPayloadBrandNewEvent, _Mapping]] = ..., event_8: _Optional[_Union[EventPayloadTestCase, _Mapping]] = ..., event_9: _Optional[_Union[EventPayloadEmptyParamEvent, _Mapping]] = ..., event_10: _Optional[_Union[EventPayloadStrParamEvent, _Mapping]] = ..., event_11: _Optional[_Union[EventPayloadBoolParamEvent, _Mapping]] = ..., event_12: _Optional[_Union[EventPayloadIntParamEvent, _Mapping]] = ..., event_13: _Optional[_Union[EventPayloadTimestampParamEvent, _Mapping]] = ..., event_14: _Optional[_Union[EventPayloadDecimalParamEvent, _Mapping]] = ..., event_15: _Optional[_Union[EventPayloadEnumParamEvent, _Mapping]] = ..., event_16: _Optional[_Union[EventPayloadBoolListEvent, _Mapping]] = ..., event_17: _Optional[_Union[EventPayloadDecimalListEvent, _Mapping]] = ..., event_18: _Optional[_Union[EventPayloadEnumListEvent, _Mapping]] = ..., event_19: _Optional[_Union[EventPayloadIntListEvent, _Mapping]] = ..., event_20: _Optional[_Union[EventPayloadStrListEvent, _Mapping]] = ..., event_21: _Optional[_Union[EventPayloadTimestampListEvent, _Mapping]] = ..., event_22: _Optional[_Union[EventPayloadBoolMapEvent, _Mapping]] = ..., event_23: _Optional[_Union[EventPayloadDecimalMapEvent, _Mapping]] = ..., event_24: _Optional[_Union[EventPayloadEnumMapEvent, _Mapping]] = ..., event_25: _Optional[_Union[EventPayloadIntMapEvent, _Mapping]] = ..., event_26: _Optional[_Union[EventPayloadStrMapEvent, _Mapping]] = ..., event_27: _Optional[_Union[EventPayloadTimestampMapEvent, _Mapping]] = ..., event_28: _Optional[_Union[EventPayloadDeprecatedEvent, _Mapping]] = ..., event_29: _Optional[_Union[EventPayloadDeprecatedPropertyEvent, _Mapping]] = ..., event_30: _Optional[_Union[EventPayloadKotlinKeywordEvent, _Mapping]] = ..., event_31: _Optional[_Union[EventPayloadJavascriptKeywordEvent, _Mapping]] = ..., event_32: _Optional[_Union[EventPayloadSwiftKeywordEvent, _Mapping]] = ..., event_33: _Optional[_Union[EventPayloadPythonKeywordEvent, _Mapping]] = ..., event_34: _Optional[_Union[EventPayloadIosOnlyEvent, _Mapping]] = ...) -> None: ...

class EventPayloadBoolListEvent(_message.Message):
    __slots__ = ["bool_list"]
    BOOL_LIST_FIELD_NUMBER: _ClassVar[int]
    bool_list: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, bool_list: _Optional[_Iterable[bool]] = ...) -> None: ...

class EventPayloadBoolMapEvent(_message.Message):
    __slots__ = ["bool_map"]
    class BoolMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    BOOL_MAP_FIELD_NUMBER: _ClassVar[int]
    bool_map: _containers.ScalarMap[str, bool]
    def __init__(self, bool_map: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class EventPayloadBoolParamEvent(_message.Message):
    __slots__ = ["bool"]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    def __init__(self, bool: bool = ...) -> None: ...

class EventPayloadBrandNewEvent(_message.Message):
    __slots__ = ["brand_id", "brand_name", "brand_type", "str", "table"]
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    BRAND_NAME_FIELD_NUMBER: _ClassVar[int]
    BRAND_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    brand_id: int
    brand_name: str
    brand_type: str
    str: str
    table: str
    def __init__(self, brand_id: _Optional[int] = ..., brand_name: _Optional[str] = ..., brand_type: _Optional[str] = ..., table: _Optional[str] = ..., str: _Optional[str] = ..., **kwargs) -> None: ...

class EventPayloadDecimalListEvent(_message.Message):
    __slots__ = ["decimal_list"]
    DECIMAL_LIST_FIELD_NUMBER: _ClassVar[int]
    decimal_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, decimal_list: _Optional[_Iterable[str]] = ...) -> None: ...

class EventPayloadDecimalMapEvent(_message.Message):
    __slots__ = ["decimal_map"]
    class DecimalMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DECIMAL_MAP_FIELD_NUMBER: _ClassVar[int]
    decimal_map: _containers.ScalarMap[str, str]
    def __init__(self, decimal_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EventPayloadDecimalParamEvent(_message.Message):
    __slots__ = ["decimal"]
    DECIMAL_FIELD_NUMBER: _ClassVar[int]
    decimal: str
    def __init__(self, decimal: _Optional[str] = ...) -> None: ...

class EventPayloadDeprecatedEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventPayloadDeprecatedPropertyEvent(_message.Message):
    __slots__ = ["deprecated_property", "not_deprecated_property"]
    DEPRECATED_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    NOT_DEPRECATED_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    deprecated_property: bool
    not_deprecated_property: bool
    def __init__(self, deprecated_property: bool = ..., not_deprecated_property: bool = ...) -> None: ...

class EventPayloadEdgeCase(_message.Message):
    __slots__ = ["prop_boolean", "prop_boolean_array", "prop_boolean_map", "prop_decimal_1", "prop_decimal_2", "prop_decimal_3", "prop_decimal_4", "prop_decimal_array", "prop_decimal_map", "prop_enum", "prop_enum_array", "prop_enum_map", "prop_integer", "prop_integer_array", "prop_integer_map", "prop_string", "prop_string_array", "prop_string_map", "prop_timestamp", "prop_timestamp_array", "prop_timestamp_map"]
    class PropBooleanMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class PropDecimalMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PropEnumMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PropIntegerMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class PropStringMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PropTimestampMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    PROP_BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PROP_BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    PROP_BOOLEAN_MAP_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_1_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_2_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_3_FIELD_NUMBER: _ClassVar[int]
    PROP_DECIMAL_4_FIELD_NUMBER: _ClassVar[int]
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
    prop_boolean_map: _containers.ScalarMap[str, bool]
    prop_decimal_1: str
    prop_decimal_2: str
    prop_decimal_3: str
    prop_decimal_4: str
    prop_decimal_array: _containers.RepeatedScalarFieldContainer[str]
    prop_decimal_map: _containers.ScalarMap[str, str]
    prop_enum: int
    prop_enum_array: _containers.RepeatedScalarFieldContainer[int]
    prop_enum_map: _containers.ScalarMap[str, int]
    prop_integer: int
    prop_integer_array: _containers.RepeatedScalarFieldContainer[int]
    prop_integer_map: _containers.ScalarMap[str, int]
    prop_string: str
    prop_string_array: _containers.RepeatedScalarFieldContainer[str]
    prop_string_map: _containers.ScalarMap[str, str]
    prop_timestamp: int
    prop_timestamp_array: _containers.RepeatedScalarFieldContainer[int]
    prop_timestamp_map: _containers.ScalarMap[str, int]
    def __init__(self, prop_boolean: bool = ..., prop_decimal_1: _Optional[str] = ..., prop_decimal_2: _Optional[str] = ..., prop_enum: _Optional[int] = ..., prop_integer: _Optional[int] = ..., prop_string: _Optional[str] = ..., prop_timestamp: _Optional[int] = ..., prop_boolean_array: _Optional[_Iterable[bool]] = ..., prop_decimal_array: _Optional[_Iterable[str]] = ..., prop_enum_array: _Optional[_Iterable[int]] = ..., prop_integer_array: _Optional[_Iterable[int]] = ..., prop_string_array: _Optional[_Iterable[str]] = ..., prop_timestamp_array: _Optional[_Iterable[int]] = ..., prop_boolean_map: _Optional[_Mapping[str, bool]] = ..., prop_decimal_map: _Optional[_Mapping[str, str]] = ..., prop_enum_map: _Optional[_Mapping[str, int]] = ..., prop_integer_map: _Optional[_Mapping[str, int]] = ..., prop_string_map: _Optional[_Mapping[str, str]] = ..., prop_timestamp_map: _Optional[_Mapping[str, int]] = ..., prop_decimal_3: _Optional[str] = ..., prop_decimal_4: _Optional[str] = ...) -> None: ...

class EventPayloadEmptyParamEvent(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventPayloadEnumListEvent(_message.Message):
    __slots__ = ["enum_list"]
    ENUM_LIST_FIELD_NUMBER: _ClassVar[int]
    enum_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, enum_list: _Optional[_Iterable[int]] = ...) -> None: ...

class EventPayloadEnumMapEvent(_message.Message):
    __slots__ = ["enum_map"]
    class EnumMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENUM_MAP_FIELD_NUMBER: _ClassVar[int]
    enum_map: _containers.ScalarMap[str, int]
    def __init__(self, enum_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EventPayloadEnumParamEvent(_message.Message):
    __slots__ = ["int"]
    INT_FIELD_NUMBER: _ClassVar[int]
    int: int
    def __init__(self, int: _Optional[int] = ...) -> None: ...

class EventPayloadIntListEvent(_message.Message):
    __slots__ = ["int_list"]
    INT_LIST_FIELD_NUMBER: _ClassVar[int]
    int_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, int_list: _Optional[_Iterable[int]] = ...) -> None: ...

class EventPayloadIntMapEvent(_message.Message):
    __slots__ = ["int_map"]
    class IntMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    INT_MAP_FIELD_NUMBER: _ClassVar[int]
    int_map: _containers.ScalarMap[str, int]
    def __init__(self, int_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EventPayloadIntParamEvent(_message.Message):
    __slots__ = ["int"]
    INT_FIELD_NUMBER: _ClassVar[int]
    int: int
    def __init__(self, int: _Optional[int] = ...) -> None: ...

class EventPayloadIosOnlyEvent(_message.Message):
    __slots__ = ["string_prop", "test_property"]
    STRING_PROP_FIELD_NUMBER: _ClassVar[int]
    TEST_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    string_prop: str
    test_property: int
    def __init__(self, test_property: _Optional[int] = ..., string_prop: _Optional[str] = ...) -> None: ...

class EventPayloadJavascriptKeywordEvent(_message.Message):
    __slots__ = ["case", "catch", "const", "debugger", "default", "delete", "do", "enum", "export", "extends", "false", "function", "implements", "instanceof", "interface", "let", "new", "null", "package", "private", "protected", "public", "static", "super", "switch", "this", "throw", "true", "typeof", "var", "void"]
    AWAIT_FIELD_NUMBER: _ClassVar[int]
    BREAK_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    CATCH_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONST_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    DEBUGGER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    DO_FIELD_NUMBER: _ClassVar[int]
    ELSE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    EXTENDS_FIELD_NUMBER: _ClassVar[int]
    FALSE_FIELD_NUMBER: _ClassVar[int]
    FINALLY_FIELD_NUMBER: _ClassVar[int]
    FOR_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    IF_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    INSTANCEOF_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    LET_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    STATIC_FIELD_NUMBER: _ClassVar[int]
    SUPER_FIELD_NUMBER: _ClassVar[int]
    SWITCH_FIELD_NUMBER: _ClassVar[int]
    THIS_FIELD_NUMBER: _ClassVar[int]
    THROW_FIELD_NUMBER: _ClassVar[int]
    TRUE_FIELD_NUMBER: _ClassVar[int]
    TRY_FIELD_NUMBER: _ClassVar[int]
    TYPEOF_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    VOID_FIELD_NUMBER: _ClassVar[int]
    WHILE_FIELD_NUMBER: _ClassVar[int]
    WITH_FIELD_NUMBER: _ClassVar[int]
    YIELD_FIELD_NUMBER: _ClassVar[int]
    case: bool
    catch: bool
    const: bool
    debugger: bool
    default: bool
    delete: bool
    do: bool
    enum: bool
    export: bool
    extends: bool
    false: bool
    function: bool
    implements: bool
    instanceof: bool
    interface: bool
    let: bool
    new: bool
    null: bool
    package: bool
    private: bool
    protected: bool
    public: bool
    static: bool
    super: bool
    switch: bool
    this: bool
    throw: bool
    true: bool
    typeof: bool
    var: bool
    void: bool
    def __init__(self, case: bool = ..., catch: bool = ..., const: bool = ..., debugger: bool = ..., default: bool = ..., delete: bool = ..., do: bool = ..., enum: bool = ..., export: bool = ..., extends: bool = ..., false: bool = ..., function: bool = ..., implements: bool = ..., instanceof: bool = ..., interface: bool = ..., let: bool = ..., new: bool = ..., null: bool = ..., package: bool = ..., private: bool = ..., protected: bool = ..., public: bool = ..., super: bool = ..., switch: bool = ..., static: bool = ..., this: bool = ..., throw: bool = ..., true: bool = ..., typeof: bool = ..., var: bool = ..., void: bool = ..., **kwargs) -> None: ...

class EventPayloadKotlinKeywordEvent(_message.Message):
    __slots__ = ["do", "false", "fun", "interface", "null", "object", "package", "super", "this", "throw", "true", "typealias", "typeof", "val", "var", "when"]
    AS_FIELD_NUMBER: _ClassVar[int]
    BREAK_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    DO_FIELD_NUMBER: _ClassVar[int]
    ELSE_FIELD_NUMBER: _ClassVar[int]
    FALSE_FIELD_NUMBER: _ClassVar[int]
    FOR_FIELD_NUMBER: _ClassVar[int]
    FUN_FIELD_NUMBER: _ClassVar[int]
    IF_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    IS_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    SUPER_FIELD_NUMBER: _ClassVar[int]
    THIS_FIELD_NUMBER: _ClassVar[int]
    THROW_FIELD_NUMBER: _ClassVar[int]
    TRUE_FIELD_NUMBER: _ClassVar[int]
    TRY_FIELD_NUMBER: _ClassVar[int]
    TYPEALIAS_FIELD_NUMBER: _ClassVar[int]
    TYPEOF_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    WHEN_FIELD_NUMBER: _ClassVar[int]
    WHILE_FIELD_NUMBER: _ClassVar[int]
    do: bool
    false: bool
    fun: bool
    interface: bool
    null: bool
    object: bool
    package: bool
    super: bool
    this: bool
    throw: bool
    true: bool
    typealias: bool
    typeof: bool
    val: bool
    var: bool
    when: bool
    def __init__(self, do: bool = ..., false: bool = ..., fun: bool = ..., interface: bool = ..., null: bool = ..., object: bool = ..., package: bool = ..., super: bool = ..., this: bool = ..., throw: bool = ..., true: bool = ..., typealias: bool = ..., typeof: bool = ..., val: bool = ..., var: bool = ..., when: bool = ..., **kwargs) -> None: ...

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

class EventPayloadPythonKeywordEvent(_message.Message):
    __slots__ = []
    AND_FIELD_NUMBER: _ClassVar[int]
    ASSERT_FIELD_NUMBER: _ClassVar[int]
    ASYNC_FIELD_NUMBER: _ClassVar[int]
    AS_FIELD_NUMBER: _ClassVar[int]
    AWAIT_FIELD_NUMBER: _ClassVar[int]
    BREAK_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    DEF_FIELD_NUMBER: _ClassVar[int]
    DEL_FIELD_NUMBER: _ClassVar[int]
    ELIF_FIELD_NUMBER: _ClassVar[int]
    ELSE_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    FINALLY_FIELD_NUMBER: _ClassVar[int]
    FOR_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    IF_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    IS_FIELD_NUMBER: _ClassVar[int]
    LAMBDA_FIELD_NUMBER: _ClassVar[int]
    NONLOCAL_FIELD_NUMBER: _ClassVar[int]
    NOT_FIELD_NUMBER: _ClassVar[int]
    OR_FIELD_NUMBER: _ClassVar[int]
    PASS_FIELD_NUMBER: _ClassVar[int]
    RAISE_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    TRY_FIELD_NUMBER: _ClassVar[int]
    WHILE_FIELD_NUMBER: _ClassVar[int]
    WITH_FIELD_NUMBER: _ClassVar[int]
    YIELD_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class EventPayloadSessionStart(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventPayloadStrListEvent(_message.Message):
    __slots__ = ["str_list"]
    STR_LIST_FIELD_NUMBER: _ClassVar[int]
    str_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, str_list: _Optional[_Iterable[str]] = ...) -> None: ...

class EventPayloadStrMapEvent(_message.Message):
    __slots__ = ["str_map"]
    class StrMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STR_MAP_FIELD_NUMBER: _ClassVar[int]
    str_map: _containers.ScalarMap[str, str]
    def __init__(self, str_map: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EventPayloadStrParamEvent(_message.Message):
    __slots__ = ["str"]
    STR_FIELD_NUMBER: _ClassVar[int]
    str: str
    def __init__(self, str: _Optional[str] = ...) -> None: ...

class EventPayloadSwiftKeywordEvent(_message.Message):
    __slots__ = ["associativity", "case", "convenience", "default", "deinit", "did_set", "do", "dynamic", "dynamic_type", "enum", "extension", "false", "final", "func", "get", "infix", "init", "inout", "internal", "lazy", "left", "let", "mutating", "nil", "none", "nonmutating", "operator", "optional", "override", "postfix", "precedence", "prefix", "private", "protocol", "public", "required", "right", "self", "set", "static", "struct", "subscript", "super", "switch", "true", "type", "typealias", "unowned", "var", "weak", "where", "will_set"]
    ASSOCIATIVITY_FIELD_NUMBER: _ClassVar[int]
    AS_FIELD_NUMBER: _ClassVar[int]
    BREAK_FIELD_NUMBER: _ClassVar[int]
    CASE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    CONVENIENCE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DEINIT_FIELD_NUMBER: _ClassVar[int]
    DID_SET_FIELD_NUMBER: _ClassVar[int]
    DO_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    ELSE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FALSE_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIELD_NUMBER: _ClassVar[int]
    FOR_FIELD_NUMBER: _ClassVar[int]
    FUNC_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    IF_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    INFIX_FIELD_NUMBER: _ClassVar[int]
    INIT_FIELD_NUMBER: _ClassVar[int]
    INOUT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    IS_FIELD_NUMBER: _ClassVar[int]
    LAZY_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    LET_FIELD_NUMBER: _ClassVar[int]
    MUTATING_FIELD_NUMBER: _ClassVar[int]
    NIL_FIELD_NUMBER: _ClassVar[int]
    NONE_FIELD_NUMBER: _ClassVar[int]
    NONMUTATING_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    POSTFIX_FIELD_NUMBER: _ClassVar[int]
    PRECEDENCE_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    STATIC_FIELD_NUMBER: _ClassVar[int]
    STRUCT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPT_FIELD_NUMBER: _ClassVar[int]
    SUPER_FIELD_NUMBER: _ClassVar[int]
    SWITCH_FIELD_NUMBER: _ClassVar[int]
    TRUE_FIELD_NUMBER: _ClassVar[int]
    TYPEALIAS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNOWNED_FIELD_NUMBER: _ClassVar[int]
    VAR_FIELD_NUMBER: _ClassVar[int]
    WEAK_FIELD_NUMBER: _ClassVar[int]
    WHERE_FIELD_NUMBER: _ClassVar[int]
    WHILE_FIELD_NUMBER: _ClassVar[int]
    WILL_SET_FIELD_NUMBER: _ClassVar[int]
    associativity: bool
    case: bool
    convenience: bool
    default: bool
    deinit: bool
    did_set: bool
    do: bool
    dynamic: bool
    dynamic_type: bool
    enum: bool
    extension: bool
    false: bool
    final: bool
    func: bool
    get: bool
    infix: bool
    init: bool
    inout: bool
    internal: bool
    lazy: bool
    left: bool
    let: bool
    mutating: bool
    nil: bool
    none: bool
    nonmutating: bool
    operator: bool
    optional: bool
    override: bool
    postfix: bool
    precedence: bool
    prefix: bool
    private: bool
    protocol: bool
    public: bool
    required: bool
    right: bool
    self: bool
    set: bool
    static: bool
    struct: bool
    subscript: bool
    super: bool
    switch: bool
    true: bool
    type: bool
    typealias: bool
    unowned: bool
    var: bool
    weak: bool
    where: bool
    will_set: bool
    def __init__(self, deinit: bool = ..., enum: bool = ..., extension: bool = ..., func: bool = ..., init: bool = ..., operator: bool = ..., private: bool = ..., protocol: bool = ..., public: bool = ..., static: bool = ..., struct: bool = ..., subscript: bool = ..., case: bool = ..., default: bool = ..., do: bool = ..., switch: bool = ..., where: bool = ..., false: bool = ..., dynamic_type: bool = ..., super: bool = ..., true: bool = ..., let: bool = ..., internal: bool = ..., typealias: bool = ..., nil: bool = ..., var: bool = ..., self: bool = ..., unowned: bool = ..., associativity: bool = ..., convenience: bool = ..., dynamic: bool = ..., did_set: bool = ..., precedence: bool = ..., final: bool = ..., get: bool = ..., infix: bool = ..., inout: bool = ..., right: bool = ..., set: bool = ..., type: bool = ..., lazy: bool = ..., left: bool = ..., mutating: bool = ..., none: bool = ..., weak: bool = ..., will_set: bool = ..., prefix: bool = ..., nonmutating: bool = ..., optional: bool = ..., override: bool = ..., postfix: bool = ..., required: bool = ..., **kwargs) -> None: ...

class EventPayloadTestCase(_message.Message):
    __slots__ = ["test_1"]
    TEST_1_FIELD_NUMBER: _ClassVar[int]
    test_1: int
    def __init__(self, test_1: _Optional[int] = ...) -> None: ...

class EventPayloadTimestampListEvent(_message.Message):
    __slots__ = ["timestamp_list"]
    TIMESTAMP_LIST_FIELD_NUMBER: _ClassVar[int]
    timestamp_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, timestamp_list: _Optional[_Iterable[int]] = ...) -> None: ...

class EventPayloadTimestampMapEvent(_message.Message):
    __slots__ = ["timestamp_map"]
    class TimestampMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TIMESTAMP_MAP_FIELD_NUMBER: _ClassVar[int]
    timestamp_map: _containers.ScalarMap[str, int]
    def __init__(self, timestamp_map: _Optional[_Mapping[str, int]] = ...) -> None: ...

class EventPayloadTimestampParamEvent(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ...) -> None: ...
