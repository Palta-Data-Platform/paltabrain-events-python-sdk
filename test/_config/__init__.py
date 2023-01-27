from abc import ABC
from datetime import datetime
from decimal import Decimal
from paltabrain_sdk import BaseContext, BaseEnum, BaseEvent, BaseSentinel, set_proto
from typing import Dict, List, Optional, Union

from .config_pb2 import Context as ContextMessage, EventHeader as EventHeaderMessage, EventPayload as EventPayloadMessage

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
        """
        super().__init__()

        self._payload = {
            'brand_id': brand_id,
            'brand_name': brand_name,
            'brand_type': brand_type,
            'from': from_,
            'class': class_,
            'table': table,
        }


