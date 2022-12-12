from abc import ABC
from datetime import datetime
from decimal import Decimal
from paltabrain_sdk import BaseContext, BaseEnum, BaseEvent, set_proto
from typing import Dict, List, Optional, Union

from .config_pb2 import Context as ContextMessage, EventHeader as EventHeaderMessage, EventPayload as EventPayloadMessage


##########
# Enum
##########


class EnumResult(BaseEnum):
    UNKNOWN = 0  # Default value
    RESULT_SUCCESS = 1  # Action was finished successfully
    RESULT_SKIP = 2  # Action was skipped
    RESULT_ERROR = 3  # Error occurred during execution


##########
# Context
##########


class Context(BaseContext):
    def set_application(self, *
                        , app_id: Optional[str] = None
                        , app_version: Optional[str] = None
                        , app_platform: Optional[str] = None
                        ):
        """
        Application context
        :param app_id: Application ID
        :param app_version: Application version
        :param app_platform: Application platform (iOS, Android, Web, MobileWeb, etc.)
        """
        self._context['application'] = {
            'app_id': app_id,
            'app_version': app_version,
            'app_platform': app_platform,
        }

        return self

    def set_device(self, *
                   , device_brand: Optional[str] = None
                   , device_model: Optional[str] = None
                   , device_carrier: Optional[str] = None
                   ):
        """
        Device context
        :param device_brand: Brand of device manufacturer
        :param device_model: Specific device model
        :param device_carrier: Mobile device carrier or network
        """
        self._context['device'] = {
            'device_brand': device_brand,
            'device_model': device_model,
            'device_carrier': device_carrier,
        }

        return self

    def set_identify(self, *
                     , idfa: Optional[str] = None
                     , idfv: Optional[str] = None
                     , gaid: Optional[str] = None
                     ):
        """
        Identifiers context
        :param idfa: Apple Identifier for Advertisers
        :param idfv: Apple Identifier for Vendors
        :param gaid: Google Advertising Identifier
        """
        self._context['identify'] = {
            'idfa': idfa,
            'idfv': idfv,
            'gaid': gaid,
        }

        return self

    def set_os(self, *
               , os_name: Optional[str] = None
               , os_version: Optional[str] = None
               ):
        """
        Operating system context
        :param os_name: Operating system name
        :param os_version: Operating system version
        """
        self._context['os'] = {
            'os_name': os_name,
            'os_version': os_version,
        }

        return self

    def set_appsflyer(self, *
                      , appsflyer_id: Optional[str] = None
                      , appsflyer_media_source: Optional[str] = None
                      ):
        """
        Appsflyer context
        :param appsflyer_id:
        :param appsflyer_media_source:
        """
        self._context['appsflyer'] = {
            'appsflyer_id': appsflyer_id,
            'appsflyer_media_source': appsflyer_media_source,
        }

        return self

    def set_user(self, *
                 , user_id: Optional[str] = None
                 ):
        """
        User context
        :param user_id: User Identifier
        """
        self._context['user'] = {
            'user_id': user_id,
        }

        return self

    def serialize_context(self):
        context_message = ContextMessage()

        for group_name, group_properties in self._context.items():
            set_proto(getattr(context_message, group_name), group_properties)

        return context_message.SerializeToString()


##########
# Event
##########


class Event(BaseEvent, ABC):
    def set_parent(self, *
                   , parent_elements: Optional[List[str]] = None
                   ):
        """
        :param parent_elements:
        """
        self._header['parent'] = {
            'parent_elements': parent_elements,
        }

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
        Very long description, very long description, very long description, very long description, very long description, very long description, very long description, very long description, very long description, very long description
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
                 , prop_enum: Optional[Union[EnumResult, int]] = None
                 , prop_integer: Optional[int] = None
                 , prop_string: Optional[str] = None
                 , prop_timestamp: Optional[Union[datetime, int]] = None
                 , prop_boolean_array: Optional[List[bool]] = None
                 , prop_decimal_array: Optional[List[Decimal]] = None
                 , prop_enum_array: Optional[List[Union[EnumResult, int]]] = None
                 , prop_integer_array: Optional[List[int]] = None
                 , prop_string_array: Optional[List[str]] = None
                 , prop_timestamp_array: Optional[List[Union[datetime, int]]] = None
                 , prop_boolean_map: Optional[Dict[str, bool]] = None
                 , prop_decimal_map: Optional[Dict[str, Decimal]] = None
                 , prop_enum_map: Optional[Dict[str, Union[EnumResult, int]]] = None
                 , prop_integer_map: Optional[Dict[str, int]] = None
                 , prop_string_map: Optional[Dict[str, str]] = None
                 , prop_timestamp_map: Optional[Dict[str, Union[datetime, int]]] = None
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
        :param prop_boolean_map: Array boolean
        :param prop_decimal_map: Array decimal
        :param prop_enum_map: Array enum
        :param prop_integer_map: Array integer
        :param prop_string_map: Array string
        :param prop_timestamp_map: Array timestamp
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
        }


