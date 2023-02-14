from abc import ABC
from datetime import datetime
from decimal import Decimal
from paltabrain_sdk import BaseContext, BaseEnum, BaseEvent, BaseSentinel, set_proto
from typing import Dict, List, Optional, Union

from .config_v2_pb2 import Context as ContextMessage, EventHeader as EventHeaderMessage, EventPayload as EventPayloadMessage

UNDEFINED = BaseSentinel()  # Sentinel object

##########
# Enum
##########


class EnumResult(BaseEnum):
    """
    {DEPRECATED} Test result

    :var RESULT_SUCCESS: Action was finished successfully
    :var RESULT_SKIP: Action was skipped
    :var RESULT_ERROR: {DEPRECATED} Error occurred during execution
    """
    UNKNOWN = 0
    RESULT_SUCCESS = 1
    RESULT_SKIP = 2
    RESULT_ERROR = 3


class EnumScreen(BaseEnum):
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ut nunc tincidunt, mattis urna at, cursus enim.
    Integer sit amet mollis justo, vel iaculis est. Phasellus in nisi nec enim tristique posuere ut ut arcu. Donec in
    elementum tortor. Nunc a tincidunt massa. Suspendisse eu ipsum sit amet magna gravida eleifend vitae at arcu. Aenean
    id malesuada enim. Cras vel scelerisque metus. Donec id lorem id quam rhoncus sollicitudin fermentum vel [...]

    :var LOGIN_SCREEN: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ut nunc tincidunt, mattis urna at, cursus enim. [...]
    :var LOGOUT_SCREEN:
    :var MAIN_SCREEN:
    """
    UNKNOWN = 0
    LOGIN_SCREEN = 1
    LOGOUT_SCREEN = 2
    MAIN_SCREEN = 3


##########
# Context
##########


class Context(BaseContext):
    def set_application(self, *
                        , app_id: Optional[str] = UNDEFINED
                        , app_version: Optional[str] = UNDEFINED
                        , app_platform: Optional[str] = UNDEFINED
                        ):
        """
        Application context

        :param app_id: Application ID
        :param app_version: Application version
        :param app_platform: Application platform (iOS, Android, Web, MobileWeb, etc.)
        """
        self._context['application'].update(BaseSentinel.filter({
            'app_id': app_id,
            'app_version': app_version,
            'app_platform': app_platform,
        }))

        return self

    def set_device(self, *
                   , device_brand: Optional[str] = UNDEFINED
                   , device_model: Optional[str] = UNDEFINED
                   , device_carrier: Optional[str] = UNDEFINED
                   ):
        """
        Device context

        :param device_brand: Brand of device manufacturer
        :param device_model: Specific device model
        :param device_carrier: Mobile device carrier or network
        """
        self._context['device'].update(BaseSentinel.filter({
            'device_brand': device_brand,
            'device_model': device_model,
            'device_carrier': device_carrier,
        }))

        return self

    def set_identify(self, *
                     , idfa: Optional[str] = UNDEFINED
                     , idfv: Optional[str] = UNDEFINED
                     , gaid: Optional[str] = UNDEFINED
                     ):
        """
        Identifiers context

        :param idfa: Apple Identifier for Advertisers
        :param idfv: Apple Identifier for Vendors
        :param gaid: Google Advertising Identifier
        """
        self._context['identify'].update(BaseSentinel.filter({
            'idfa': idfa,
            'idfv': idfv,
            'gaid': gaid,
        }))

        return self

    def set_os(self, *
               , os_name: Optional[str] = UNDEFINED
               , os_version: Optional[str] = UNDEFINED
               ):
        """
        Operating system context

        :param os_name: Operating system name
        :param os_version: Operating system version
        """
        self._context['os'].update(BaseSentinel.filter({
            'os_name': os_name,
            'os_version': os_version,
        }))

        return self

    def set_appsflyer(self, *
                      , appsflyer_id: Optional[str] = UNDEFINED
                      , appsflyer_media_source: Optional[str] = UNDEFINED
                      ):
        """
        Appsflyer context

        :param appsflyer_id:
        :param appsflyer_media_source:
        """
        self._context['appsflyer'].update(BaseSentinel.filter({
            'appsflyer_id': appsflyer_id,
            'appsflyer_media_source': appsflyer_media_source,
        }))

        return self

    def set_user(self, *
                 , user_id: Optional[str] = UNDEFINED
                 ):
        """
        User context

        :param user_id: User Identifier
        """
        self._context['user'].update(BaseSentinel.filter({
            'user_id': user_id,
        }))

        return self

    def serialize_context(self):
        context_message = ContextMessage()

        for group_name, group_properties in self._context.items():
            set_proto(getattr(context_message, group_name), group_properties)

        return context_message.SerializeToString(deterministic=True)


##########
# Event
##########


class Event(BaseEvent, ABC):
    def set_parent(self, *
                   , parent_elements: Optional[List[str]] = UNDEFINED
                   ):
        """
        :param parent_elements:
        """
        self._header['parent'].update(BaseSentinel.filter({
            'parent_elements': parent_elements,
        }))

        return self

    def set_onboarding(self, *
                       , onboarding_id: Optional[int] = UNDEFINED
                       , onboarding_version: Optional[str] = UNDEFINED
                       ):
        """
        :param onboarding_id:
        :param onboarding_version:
        """
        self._header['onboarding'].update(BaseSentinel.filter({
            'onboarding_id': onboarding_id,
            'onboarding_version': onboarding_version,
        }))

        return self

    def set_edge_case(self, *
                      , prop_boolean: Optional[bool] = UNDEFINED
                      , prop_decimal_1: Optional[Decimal] = UNDEFINED
                      , prop_decimal_2: Optional[Decimal] = UNDEFINED
                      , prop_enum: Optional[EnumResult] = UNDEFINED
                      , prop_integer: Optional[int] = UNDEFINED
                      , prop_string: Optional[str] = UNDEFINED
                      , prop_timestamp: Optional[datetime] = UNDEFINED
                      , prop_integer_array: Optional[List[int]] = UNDEFINED
                      , prop_integer_map: Optional[Dict[str, int]] = UNDEFINED
                      ):
        """
        :param prop_boolean:
        :param prop_decimal_1:
        :param prop_decimal_2:
        :param prop_enum:
        :param prop_integer:
        :param prop_string:
        :param prop_timestamp:
        :param prop_integer_array:
        :param prop_integer_map:
        """
        self._header['edge_case'].update(BaseSentinel.filter({
            'prop_boolean': prop_boolean,
            'prop_decimal_1': prop_decimal_1,
            'prop_decimal_2': prop_decimal_2,
            'prop_enum': prop_enum,
            'prop_integer': prop_integer,
            'prop_string': prop_string,
            'prop_timestamp': prop_timestamp,
            'prop_integer_array': prop_integer_array,
            'prop_integer_map': prop_integer_map,
        }))

        return self

    def serialize_header(self):
        if not self._header:
            return b""

        header_message = EventHeaderMessage()

        for group_name, group_properties in self._header.items():
            set_proto(getattr(header_message, group_name), group_properties)

        return header_message.SerializeToString()

    def serialize_payload(self):
        payload_message = EventPayloadMessage()

        getattr(payload_message, f"event_{self.event_type_id}").SetInParent()
        set_proto(getattr(payload_message, f"event_{self.event_type_id}"), self._payload)

        return payload_message.SerializeToString()


class EventSessionStart(Event):
    event_type_id = 1

    def __init__(self):
        """
        """
        super().__init__()


class EventOnboardingStart(Event):
    event_type_id = 2

    def __init__(self):
        """
        """
        super().__init__()


class EventOnboardingFinish(Event):
    event_type_id = 3

    def __init__(self):
        """
        """
        super().__init__()


class EventPageOpen(Event):
    event_type_id = 4

    def __init__(self, *
                 , page_id: Optional[str] = None
                 ):
        """
        :param page_id:
        """
        super().__init__()

        self._payload = {
            'page_id': page_id,
        }


class EventPermissionsRequest(Event):
    event_type_id = 5

    def __init__(self, *
                 , is_granted: Optional[bool] = None
                 , type: Optional[str] = None
                 ):
        """
        Very long description, very long description, very long description, very long description, very long description, very
        long description, very long description, very long description, very long description, very long description

        :param is_granted:
        :param type:
        """
        super().__init__()

        self._payload = {
            'is_granted': is_granted,
            'type': type,
        }


class EventEdgeCase(Event):
    event_type_id = 6

    def __init__(self, *
                 , prop_boolean: Optional[bool] = None
                 , prop_decimal_1: Optional[Decimal] = None
                 , prop_decimal_2: Optional[Decimal] = None
                 , prop_enum: Optional[EnumResult] = None
                 , prop_integer: Optional[int] = None
                 , prop_string: Optional[str] = None
                 , prop_timestamp: Optional[datetime] = None
                 , prop_boolean_array: Optional[List[bool]] = None
                 , prop_decimal_array: Optional[List[Decimal]] = None
                 , prop_enum_array: Optional[List[EnumResult]] = None
                 , prop_integer_array: Optional[List[int]] = None
                 , prop_string_array: Optional[List[str]] = None
                 , prop_timestamp_array: Optional[List[datetime]] = None
                 , prop_boolean_map: Optional[Dict[str, bool]] = None
                 , prop_decimal_map: Optional[Dict[str, Decimal]] = None
                 , prop_enum_map: Optional[Dict[str, EnumResult]] = None
                 , prop_integer_map: Optional[Dict[str, int]] = None
                 , prop_string_map: Optional[Dict[str, str]] = None
                 , prop_timestamp_map: Optional[Dict[str, datetime]] = None
                 , prop_decimal_3: Optional[Decimal] = None
                 , prop_decimal_4: Optional[Decimal] = None
                 ):
        """
        Special testing event with all types of properties

        :param prop_boolean: Plain boolean
        :param prop_decimal_1: Decimal with fractional part
        :param prop_decimal_2: Decimal without fractional part
        :param prop_enum: Plain enum
        :param prop_integer: Plain integer
        :param prop_string: Plain string
        :param prop_timestamp: Plain timestamp
        :param prop_boolean_array: Array boolean
        :param prop_decimal_array: Array decimal
        :param prop_enum_array: Array enum
        :param prop_integer_array: Array integer
        :param prop_string_array: Array string
        :param prop_timestamp_array: Array timestamp
        :param prop_boolean_map: Map boolean
        :param prop_decimal_map: Map decimal
        :param prop_enum_map: Map enum
        :param prop_integer_map: Map integer
        :param prop_string_map: Map string
        :param prop_timestamp_map: Map timestamp
        :param prop_decimal_3:
        :param prop_decimal_4:
        """
        super().__init__()

        self._payload = {
            'prop_boolean': prop_boolean,
            'prop_decimal_1': prop_decimal_1,
            'prop_decimal_2': prop_decimal_2,
            'prop_enum': prop_enum,
            'prop_integer': prop_integer,
            'prop_string': prop_string,
            'prop_timestamp': prop_timestamp,
            'prop_boolean_array': prop_boolean_array,
            'prop_decimal_array': prop_decimal_array,
            'prop_enum_array': prop_enum_array,
            'prop_integer_array': prop_integer_array,
            'prop_string_array': prop_string_array,
            'prop_timestamp_array': prop_timestamp_array,
            'prop_boolean_map': prop_boolean_map,
            'prop_decimal_map': prop_decimal_map,
            'prop_enum_map': prop_enum_map,
            'prop_integer_map': prop_integer_map,
            'prop_string_map': prop_string_map,
            'prop_timestamp_map': prop_timestamp_map,
            'prop_decimal_3': prop_decimal_3,
            'prop_decimal_4': prop_decimal_4,
        }


class EventBrandNewEvent(Event):
    event_type_id = 7

    def __init__(self, *
                 , brand_id: Optional[int] = None
                 , brand_name: Optional[str] = None
                 , brand_type: Optional[str] = None
                 , from_: Optional[str] = None
                 , class_: Optional[str] = None
                 , table: Optional[str] = None
                 , str: Optional[str] = None
                 ):
        """
        {DEPRECATED} Very long and crazy description, which tries to close the comment with \""", */, #.  Lorem ipsum dolor sit
        amet, consectetur adipiscing elit. Praesent ut nunc tincidunt, mattis urna at, cursus enim. Integer sit amet
        mollis justo, vel iaculis est. Phasellus in nisi nec enim tristique posuere ut ut arcu. Donec in elementum
        tortor. Nunc a tincidunt massa. Suspendisse eu ipsum sit amet magna gravida eleifend vitae at arcu. Aenean [...]

        :param brand_id:
        :param brand_name: {DEPRECATED} Crazy comment \""", */, #.  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ut nunc [...]
        :param brand_type: {DEPRECATED}
        :param from_: Property as reserved word
        :param class_: Property as reserved word
        :param table: Property as reserved word in SQL
        :param str:
        """
        super().__init__()

        self._payload = {
            'brand_id': brand_id,
            'brand_name': brand_name,
            'brand_type': brand_type,
            'from': from_,
            'class': class_,
            'table': table,
            'str': str,
        }


class EventTestCase(Event):
    event_type_id = 8

    def __init__(self, *
                 , test_1: Optional[int] = None
                 ):
        """
        :param test_1:
        """
        super().__init__()

        self._payload = {
            'test_1': test_1,
        }


class EventEmptyParamEvent(Event):
    event_type_id = 9

    def __init__(self):
        """
        """
        super().__init__()


class EventStrParamEvent(Event):
    event_type_id = 10

    def __init__(self, *
                 , str: Optional[str] = None
                 ):
        """
        :param str:
        """
        super().__init__()

        self._payload = {
            'str': str,
        }


class EventBoolParamEvent(Event):
    event_type_id = 11

    def __init__(self, *
                 , bool: Optional[bool] = None
                 ):
        """
        :param bool:
        """
        super().__init__()

        self._payload = {
            'bool': bool,
        }


class EventIntParamEvent(Event):
    event_type_id = 12

    def __init__(self, *
                 , int: Optional[int] = None
                 ):
        """
        :param int:
        """
        super().__init__()

        self._payload = {
            'int': int,
        }


class EventTimestampParamEvent(Event):
    event_type_id = 13

    def __init__(self, *
                 , timestamp: Optional[datetime] = None
                 ):
        """
        :param timestamp:
        """
        super().__init__()

        self._payload = {
            'timestamp': timestamp,
        }


class EventDecimalParamEvent(Event):
    event_type_id = 14

    def __init__(self, *
                 , decimal: Optional[Decimal] = None
                 ):
        """
        :param decimal:
        """
        super().__init__()

        self._payload = {
            'decimal': decimal,
        }


class EventEnumParamEvent(Event):
    event_type_id = 15

    def __init__(self, *
                 , int: Optional[EnumResult] = None
                 ):
        """
        :param int:
        """
        super().__init__()

        self._payload = {
            'int': int,
        }


class EventBoolListEvent(Event):
    event_type_id = 16

    def __init__(self, *
                 , bool_list: Optional[List[bool]] = None
                 ):
        """
        :param bool_list:
        """
        super().__init__()

        self._payload = {
            'bool_list': bool_list,
        }


class EventDecimalListEvent(Event):
    event_type_id = 17

    def __init__(self, *
                 , decimal_list: Optional[List[Decimal]] = None
                 ):
        """
        :param decimal_list:
        """
        super().__init__()

        self._payload = {
            'decimal_list': decimal_list,
        }


class EventEnumListEvent(Event):
    event_type_id = 18

    def __init__(self, *
                 , enum_list: Optional[List[EnumResult]] = None
                 ):
        """
        :param enum_list:
        """
        super().__init__()

        self._payload = {
            'enum_list': enum_list,
        }


class EventIntListEvent(Event):
    event_type_id = 19

    def __init__(self, *
                 , int_list: Optional[List[int]] = None
                 ):
        """
        :param int_list:
        """
        super().__init__()

        self._payload = {
            'int_list': int_list,
        }


class EventStrListEvent(Event):
    event_type_id = 20

    def __init__(self, *
                 , str_list: Optional[List[str]] = None
                 ):
        """
        :param str_list:
        """
        super().__init__()

        self._payload = {
            'str_list': str_list,
        }


class EventTimestampListEvent(Event):
    event_type_id = 21

    def __init__(self, *
                 , timestamp_list: Optional[List[datetime]] = None
                 ):
        """
        :param timestamp_list:
        """
        super().__init__()

        self._payload = {
            'timestamp_list': timestamp_list,
        }


class EventBoolMapEvent(Event):
    event_type_id = 22

    def __init__(self, *
                 , bool_map: Optional[Dict[str, bool]] = None
                 ):
        """
        :param bool_map:
        """
        super().__init__()

        self._payload = {
            'bool_map': bool_map,
        }


class EventDecimalMapEvent(Event):
    event_type_id = 23

    def __init__(self, *
                 , decimal_map: Optional[Dict[str, Decimal]] = None
                 ):
        """
        :param decimal_map:
        """
        super().__init__()

        self._payload = {
            'decimal_map': decimal_map,
        }


class EventEnumMapEvent(Event):
    event_type_id = 24

    def __init__(self, *
                 , enum_map: Optional[Dict[str, EnumResult]] = None
                 ):
        """
        :param enum_map:
        """
        super().__init__()

        self._payload = {
            'enum_map': enum_map,
        }


class EventIntMapEvent(Event):
    event_type_id = 25

    def __init__(self, *
                 , int_map: Optional[Dict[str, int]] = None
                 ):
        """
        :param int_map:
        """
        super().__init__()

        self._payload = {
            'int_map': int_map,
        }


class EventStrMapEvent(Event):
    event_type_id = 26

    def __init__(self, *
                 , str_map: Optional[Dict[str, str]] = None
                 ):
        """
        :param str_map:
        """
        super().__init__()

        self._payload = {
            'str_map': str_map,
        }


class EventTimestampMapEvent(Event):
    event_type_id = 27

    def __init__(self, *
                 , timestamp_map: Optional[Dict[str, datetime]] = None
                 ):
        """
        :param timestamp_map:
        """
        super().__init__()

        self._payload = {
            'timestamp_map': timestamp_map,
        }


class EventDeprecatedEvent(Event):
    event_type_id = 28

    def __init__(self):
        """
        {DEPRECATED}

        """
        super().__init__()


class EventDeprecatedPropertyEvent(Event):
    event_type_id = 29

    def __init__(self, *
                 , deprecated_property: Optional[bool] = None
                 , not_deprecated_property: Optional[bool] = None
                 ):
        """
        :param deprecated_property: {DEPRECATED}
        :param not_deprecated_property:
        """
        super().__init__()

        self._payload = {
            'deprecated_property': deprecated_property,
            'not_deprecated_property': not_deprecated_property,
        }


class EventKotlinKeywordEvent(Event):
    event_type_id = 30

    def __init__(self, *
                 , as_: Optional[bool] = None
                 , break_: Optional[bool] = None
                 , class_: Optional[bool] = None
                 , continue_: Optional[bool] = None
                 , do: Optional[bool] = None
                 , else_: Optional[bool] = None
                 , false: Optional[bool] = None
                 , for_: Optional[bool] = None
                 , fun: Optional[bool] = None
                 , if_: Optional[bool] = None
                 , in_: Optional[bool] = None
                 , interface: Optional[bool] = None
                 , is_: Optional[bool] = None
                 , null: Optional[bool] = None
                 , object: Optional[bool] = None
                 , package: Optional[bool] = None
                 , return_: Optional[bool] = None
                 , super: Optional[bool] = None
                 , this: Optional[bool] = None
                 , throw: Optional[bool] = None
                 , true: Optional[bool] = None
                 , typealias: Optional[bool] = None
                 , typeof: Optional[bool] = None
                 , try_: Optional[bool] = None
                 , val: Optional[bool] = None
                 , var: Optional[bool] = None
                 , while_: Optional[bool] = None
                 , when: Optional[bool] = None
                 ):
        """
        :param as_:
        :param break_:
        :param class_:
        :param continue_:
        :param do:
        :param else_:
        :param false:
        :param for_:
        :param fun:
        :param if_:
        :param in_:
        :param interface:
        :param is_:
        :param null:
        :param object:
        :param package:
        :param return_:
        :param super:
        :param this:
        :param throw:
        :param true:
        :param typealias:
        :param typeof:
        :param try_:
        :param val:
        :param var:
        :param while_:
        :param when:
        """
        super().__init__()

        self._payload = {
            'as': as_,
            'break': break_,
            'class': class_,
            'continue': continue_,
            'do': do,
            'else': else_,
            'false': false,
            'for': for_,
            'fun': fun,
            'if': if_,
            'in': in_,
            'interface': interface,
            'is': is_,
            'null': null,
            'object': object,
            'package': package,
            'return': return_,
            'super': super,
            'this': this,
            'throw': throw,
            'true': true,
            'typealias': typealias,
            'typeof': typeof,
            'try': try_,
            'val': val,
            'var': var,
            'while': while_,
            'when': when,
        }


class EventJavascriptKeywordEvent(Event):
    event_type_id = 31

    def __init__(self, *
                 , await_: Optional[bool] = None
                 , break_: Optional[bool] = None
                 , case: Optional[bool] = None
                 , catch: Optional[bool] = None
                 , class_: Optional[bool] = None
                 , const: Optional[bool] = None
                 , continue_: Optional[bool] = None
                 , debugger: Optional[bool] = None
                 , default: Optional[bool] = None
                 , delete: Optional[bool] = None
                 , do: Optional[bool] = None
                 , else_: Optional[bool] = None
                 , enum: Optional[bool] = None
                 , export: Optional[bool] = None
                 , extends: Optional[bool] = None
                 , false: Optional[bool] = None
                 , finally_: Optional[bool] = None
                 , for_: Optional[bool] = None
                 , function: Optional[bool] = None
                 , if_: Optional[bool] = None
                 , implements: Optional[bool] = None
                 , import_: Optional[bool] = None
                 , in_: Optional[bool] = None
                 , instanceof: Optional[bool] = None
                 , interface: Optional[bool] = None
                 , let: Optional[bool] = None
                 , new: Optional[bool] = None
                 , null: Optional[bool] = None
                 , package: Optional[bool] = None
                 , private: Optional[bool] = None
                 , protected: Optional[bool] = None
                 , public: Optional[bool] = None
                 , return_: Optional[bool] = None
                 , super: Optional[bool] = None
                 , switch: Optional[bool] = None
                 , static: Optional[bool] = None
                 , this: Optional[bool] = None
                 , throw: Optional[bool] = None
                 , try_: Optional[bool] = None
                 , true: Optional[bool] = None
                 , typeof: Optional[bool] = None
                 , var: Optional[bool] = None
                 , void: Optional[bool] = None
                 , while_: Optional[bool] = None
                 , with_: Optional[bool] = None
                 , yield_: Optional[bool] = None
                 ):
        """
        :param await_:
        :param break_:
        :param case:
        :param catch:
        :param class_:
        :param const:
        :param continue_:
        :param debugger:
        :param default:
        :param delete:
        :param do:
        :param else_:
        :param enum:
        :param export:
        :param extends:
        :param false:
        :param finally_:
        :param for_:
        :param function:
        :param if_:
        :param implements:
        :param import_:
        :param in_:
        :param instanceof:
        :param interface:
        :param let:
        :param new:
        :param null:
        :param package:
        :param private:
        :param protected:
        :param public:
        :param return_:
        :param super:
        :param switch:
        :param static:
        :param this:
        :param throw:
        :param try_:
        :param true:
        :param typeof:
        :param var:
        :param void:
        :param while_:
        :param with_:
        :param yield_:
        """
        super().__init__()

        self._payload = {
            'await': await_,
            'break': break_,
            'case': case,
            'catch': catch,
            'class': class_,
            'const': const,
            'continue': continue_,
            'debugger': debugger,
            'default': default,
            'delete': delete,
            'do': do,
            'else': else_,
            'enum': enum,
            'export': export,
            'extends': extends,
            'false': false,
            'finally': finally_,
            'for': for_,
            'function': function,
            'if': if_,
            'implements': implements,
            'import': import_,
            'in': in_,
            'instanceof': instanceof,
            'interface': interface,
            'let': let,
            'new': new,
            'null': null,
            'package': package,
            'private': private,
            'protected': protected,
            'public': public,
            'return': return_,
            'super': super,
            'switch': switch,
            'static': static,
            'this': this,
            'throw': throw,
            'try': try_,
            'true': true,
            'typeof': typeof,
            'var': var,
            'void': void,
            'while': while_,
            'with': with_,
            'yield': yield_,
        }


class EventSwiftKeywordEvent(Event):
    event_type_id = 32

    def __init__(self, *
                 , class_: Optional[bool] = None
                 , deinit: Optional[bool] = None
                 , enum: Optional[bool] = None
                 , extension: Optional[bool] = None
                 , func: Optional[bool] = None
                 , import_: Optional[bool] = None
                 , init: Optional[bool] = None
                 , operator: Optional[bool] = None
                 , private: Optional[bool] = None
                 , protocol: Optional[bool] = None
                 , public: Optional[bool] = None
                 , static: Optional[bool] = None
                 , struct: Optional[bool] = None
                 , subscript: Optional[bool] = None
                 , break_: Optional[bool] = None
                 , case: Optional[bool] = None
                 , continue_: Optional[bool] = None
                 , default: Optional[bool] = None
                 , do: Optional[bool] = None
                 , else_: Optional[bool] = None
                 , for_: Optional[bool] = None
                 , return_: Optional[bool] = None
                 , switch: Optional[bool] = None
                 , where: Optional[bool] = None
                 , while_: Optional[bool] = None
                 , as_: Optional[bool] = None
                 , false: Optional[bool] = None
                 , is_: Optional[bool] = None
                 , dynamic_type: Optional[bool] = None
                 , super: Optional[bool] = None
                 , true: Optional[bool] = None
                 , let: Optional[bool] = None
                 , in_: Optional[bool] = None
                 , internal: Optional[bool] = None
                 , typealias: Optional[bool] = None
                 , if_: Optional[bool] = None
                 , nil: Optional[bool] = None
                 , var: Optional[bool] = None
                 , self_: Optional[bool] = None
                 , unowned: Optional[bool] = None
                 , associativity: Optional[bool] = None
                 , convenience: Optional[bool] = None
                 , dynamic: Optional[bool] = None
                 , did_set: Optional[bool] = None
                 , precedence: Optional[bool] = None
                 , final: Optional[bool] = None
                 , get: Optional[bool] = None
                 , infix: Optional[bool] = None
                 , inout: Optional[bool] = None
                 , right: Optional[bool] = None
                 , set: Optional[bool] = None
                 , type: Optional[bool] = None
                 , lazy: Optional[bool] = None
                 , left: Optional[bool] = None
                 , mutating: Optional[bool] = None
                 , none: Optional[bool] = None
                 , weak: Optional[bool] = None
                 , will_set: Optional[bool] = None
                 , prefix: Optional[bool] = None
                 , nonmutating: Optional[bool] = None
                 , optional: Optional[bool] = None
                 , override: Optional[bool] = None
                 , postfix: Optional[bool] = None
                 , required: Optional[bool] = None
                 ):
        """
        :param class_:
        :param deinit:
        :param enum:
        :param extension:
        :param func:
        :param import_:
        :param init:
        :param operator:
        :param private:
        :param protocol:
        :param public:
        :param static:
        :param struct:
        :param subscript:
        :param break_:
        :param case:
        :param continue_:
        :param default:
        :param do:
        :param else_:
        :param for_:
        :param return_:
        :param switch:
        :param where:
        :param while_:
        :param as_:
        :param false:
        :param is_:
        :param dynamic_type:
        :param super:
        :param true:
        :param let:
        :param in_:
        :param internal:
        :param typealias:
        :param if_:
        :param nil:
        :param var:
        :param self_:
        :param unowned:
        :param associativity:
        :param convenience:
        :param dynamic:
        :param did_set:
        :param precedence:
        :param final:
        :param get:
        :param infix:
        :param inout:
        :param right:
        :param set:
        :param type:
        :param lazy:
        :param left:
        :param mutating:
        :param none:
        :param weak:
        :param will_set:
        :param prefix:
        :param nonmutating:
        :param optional:
        :param override:
        :param postfix:
        :param required:
        """
        super().__init__()

        self._payload = {
            'class': class_,
            'deinit': deinit,
            'enum': enum,
            'extension': extension,
            'func': func,
            'import': import_,
            'init': init,
            'operator': operator,
            'private': private,
            'protocol': protocol,
            'public': public,
            'static': static,
            'struct': struct,
            'subscript': subscript,
            'break': break_,
            'case': case,
            'continue': continue_,
            'default': default,
            'do': do,
            'else': else_,
            'for': for_,
            'return': return_,
            'switch': switch,
            'where': where,
            'while': while_,
            'as': as_,
            'false': false,
            'is': is_,
            'dynamic_type': dynamic_type,
            'super': super,
            'true': true,
            'let': let,
            'in': in_,
            'internal': internal,
            'typealias': typealias,
            'if': if_,
            'nil': nil,
            'var': var,
            'self': self_,
            'unowned': unowned,
            'associativity': associativity,
            'convenience': convenience,
            'dynamic': dynamic,
            'did_set': did_set,
            'precedence': precedence,
            'final': final,
            'get': get,
            'infix': infix,
            'inout': inout,
            'right': right,
            'set': set,
            'type': type,
            'lazy': lazy,
            'left': left,
            'mutating': mutating,
            'none': none,
            'weak': weak,
            'will_set': will_set,
            'prefix': prefix,
            'nonmutating': nonmutating,
            'optional': optional,
            'override': override,
            'postfix': postfix,
            'required': required,
        }


class EventPythonKeywordEvent(Event):
    event_type_id = 33

    def __init__(self, *
                 , await_: Optional[bool] = None
                 , else_: Optional[bool] = None
                 , import_: Optional[bool] = None
                 , pass_: Optional[bool] = None
                 , break_: Optional[bool] = None
                 , except_: Optional[bool] = None
                 , in_: Optional[bool] = None
                 , raise_: Optional[bool] = None
                 , class_: Optional[bool] = None
                 , finally_: Optional[bool] = None
                 , is_: Optional[bool] = None
                 , return_: Optional[bool] = None
                 , and_: Optional[bool] = None
                 , continue_: Optional[bool] = None
                 , for_: Optional[bool] = None
                 , lambda_: Optional[bool] = None
                 , try_: Optional[bool] = None
                 , as_: Optional[bool] = None
                 , def_: Optional[bool] = None
                 , from_: Optional[bool] = None
                 , nonlocal_: Optional[bool] = None
                 , while_: Optional[bool] = None
                 , assert_: Optional[bool] = None
                 , del_: Optional[bool] = None
                 , global_: Optional[bool] = None
                 , not_: Optional[bool] = None
                 , with_: Optional[bool] = None
                 , async_: Optional[bool] = None
                 , elif_: Optional[bool] = None
                 , if_: Optional[bool] = None
                 , or_: Optional[bool] = None
                 , yield_: Optional[bool] = None
                 ):
        """
        :param await_:
        :param else_:
        :param import_:
        :param pass_:
        :param break_:
        :param except_:
        :param in_:
        :param raise_:
        :param class_:
        :param finally_:
        :param is_:
        :param return_:
        :param and_:
        :param continue_:
        :param for_:
        :param lambda_:
        :param try_:
        :param as_:
        :param def_:
        :param from_:
        :param nonlocal_:
        :param while_:
        :param assert_:
        :param del_:
        :param global_:
        :param not_:
        :param with_:
        :param async_:
        :param elif_:
        :param if_:
        :param or_:
        :param yield_:
        """
        super().__init__()

        self._payload = {
            'await': await_,
            'else': else_,
            'import': import_,
            'pass': pass_,
            'break': break_,
            'except': except_,
            'in': in_,
            'raise': raise_,
            'class': class_,
            'finally': finally_,
            'is': is_,
            'return': return_,
            'and': and_,
            'continue': continue_,
            'for': for_,
            'lambda': lambda_,
            'try': try_,
            'as': as_,
            'def': def_,
            'from': from_,
            'nonlocal': nonlocal_,
            'while': while_,
            'assert': assert_,
            'del': del_,
            'global': global_,
            'not': not_,
            'with': with_,
            'async': async_,
            'elif': elif_,
            'if': if_,
            'or': or_,
            'yield': yield_,
        }


class EventIosOnlyEvent(Event):
    event_type_id = 34

    def __init__(self, *
                 , test_property: Optional[int] = None
                 , string_prop: Optional[str] = None
                 ):
        """
        This event is solely for purposes of iOS sdk testing and can be modified without prior notification. Do not use it in
        other platform tests!

        :param test_property:
        :param string_prop:
        """
        super().__init__()

        self._payload = {
            'test_property': test_property,
            'string_prop': string_prop,
        }


