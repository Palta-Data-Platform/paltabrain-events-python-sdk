# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63onfig_v1.proto\x12\x1apaltabrain.event_schema.v1\"O\n\x12\x43ontextApplication\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x02 \x01(\t\x12\x14\n\x0c\x61pp_platform\x18\x03 \x01(\t\"S\n\rContextDevice\x12\x14\n\x0c\x64\x65vice_brand\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x65vice_carrier\x18\x03 \x01(\t\";\n\x0f\x43ontextIdentify\x12\x0c\n\x04idfa\x18\x01 \x01(\t\x12\x0c\n\x04idfv\x18\x02 \x01(\t\x12\x0c\n\x04gaid\x18\x03 \x01(\t\"0\n\tContextOs\x12\x0f\n\x07os_name\x18\x01 \x01(\t\x12\x12\n\nos_version\x18\x02 \x01(\t\"H\n\x10\x43ontextAppsflyer\x12\x14\n\x0c\x61ppsflyer_id\x18\x01 \x01(\t\x12\x1e\n\x16\x61ppsflyer_media_source\x18\x02 \x01(\t\"\x1e\n\x0b\x43ontextUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xf3\x02\n\x07\x43ontext\x12\x43\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32..paltabrain.event_schema.v1.ContextApplication\x12\x39\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32).paltabrain.event_schema.v1.ContextDevice\x12=\n\x08identify\x18\x03 \x01(\x0b\x32+.paltabrain.event_schema.v1.ContextIdentify\x12\x31\n\x02os\x18\x04 \x01(\x0b\x32%.paltabrain.event_schema.v1.ContextOs\x12?\n\tappsflyer\x18\x05 \x01(\x0b\x32,.paltabrain.event_schema.v1.ContextAppsflyer\x12\x35\n\x04user\x18\x06 \x01(\x0b\x32\'.paltabrain.event_schema.v1.ContextUser\",\n\x11\x45ventHeaderParent\x12\x17\n\x0fparent_elements\x18\x01 \x03(\t\"L\n\x0b\x45ventHeader\x12=\n\x06parent\x18\x01 \x01(\x0b\x32-.paltabrain.event_schema.v1.EventHeaderParent\"\x1a\n\x18\x45ventPayloadSessionStart\"\x1d\n\x1b\x45ventPayloadOnboardingStart\"\x1e\n\x1c\x45ventPayloadOnboardingFinish\"\'\n\x14\x45ventPayloadPageOpen\x12\x0f\n\x07page_id\x18\x01 \x01(\t\"B\n\x1e\x45ventPayloadPermissionsRequest\x12\x12\n\nis_granted\x18\x01 \x01(\x08\x12\x0c\n\x04type\x18\x02 \x01(\t\"\xf2\x03\n\x14\x45ventPayloadEdgeCase\x12\x14\n\x0cprop_boolean\x18\x01 \x01(\x08\x12\x16\n\x0eprop_decimal_1\x18\x02 \x01(\t\x12\x16\n\x0eprop_decimal_2\x18\x03 \x01(\t\x12\x11\n\tprop_enum\x18\x04 \x01(\x03\x12\x14\n\x0cprop_integer\x18\x05 \x01(\x03\x12\x13\n\x0bprop_string\x18\x06 \x01(\t\x12\x16\n\x0eprop_timestamp\x18\x07 \x01(\x03\x12\x1a\n\x12prop_boolean_array\x18\x08 \x03(\x08\x12\x1a\n\x12prop_decimal_array\x18\t \x03(\t\x12\x17\n\x0fprop_enum_array\x18\n \x03(\x03\x12\x1a\n\x12prop_integer_array\x18\x0b \x03(\x03\x12\x19\n\x11prop_string_array\x18\x0c \x03(\t\x12\x1c\n\x14prop_timestamp_array\x18\r \x03(\x03\x12\x18\n\x10prop_boolean_map\x18\x0e \x01(\x08\x12\x18\n\x10prop_decimal_map\x18\x0f \x01(\t\x12\x15\n\rprop_enum_map\x18\x10 \x01(\x03\x12\x18\n\x10prop_integer_map\x18\x11 \x01(\x03\x12\x17\n\x0fprop_string_map\x18\x12 \x01(\t\x12\x1a\n\x12prop_timestamp_map\x18\x13 \x01(\x03\"f\n\x0b\x45ventCommon\x12\x12\n\nevent_type\x18\x01 \x01(\x03\x12\x10\n\x08\x65vent_ts\x18\x02 \x01(\x03\x12\x12\n\nsession_id\x18\x03 \x01(\x03\x12\x1d\n\x15session_event_seq_num\x18\x04 \x01(\x03\"\xd7\x03\n\x0c\x45ventPayload\x12G\n\x07\x65vent_1\x18\x01 \x01(\x0b\x32\x34.paltabrain.event_schema.v1.EventPayloadSessionStartH\x00\x12J\n\x07\x65vent_2\x18\x02 \x01(\x0b\x32\x37.paltabrain.event_schema.v1.EventPayloadOnboardingStartH\x00\x12K\n\x07\x65vent_3\x18\x03 \x01(\x0b\x32\x38.paltabrain.event_schema.v1.EventPayloadOnboardingFinishH\x00\x12\x43\n\x07\x65vent_4\x18\x04 \x01(\x0b\x32\x30.paltabrain.event_schema.v1.EventPayloadPageOpenH\x00\x12M\n\x07\x65vent_5\x18\x05 \x01(\x0b\x32:.paltabrain.event_schema.v1.EventPayloadPermissionsRequestH\x00\x12\x43\n\x07\x65vent_6\x18\x06 \x01(\x0b\x32\x30.paltabrain.event_schema.v1.EventPayloadEdgeCaseH\x00\x42\x0c\n\nevent_type\"\xb4\x01\n\x05\x45vent\x12\x37\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\'.paltabrain.event_schema.v1.EventCommon\x12\x37\n\x06header\x18\x02 \x01(\x0b\x32\'.paltabrain.event_schema.v1.EventHeader\x12\x39\n\x07payload\x18\x03 \x01(\x0b\x32(.paltabrain.event_schema.v1.EventPayload\"n\n\x0b\x42\x61tchCommon\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61tch_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x0e\n\x06locale\x18\x04 \x01(\t\x12\x12\n\nutc_offset\x18\x05 \x01(\x12\"\xa9\x01\n\x05\x42\x61tch\x12\x37\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\'.paltabrain.event_schema.v1.BatchCommon\x12\x34\n\x07\x63ontext\x18\x02 \x01(\x0b\x32#.paltabrain.event_schema.v1.Context\x12\x31\n\x06\x65vents\x18\x03 \x03(\x0b\x32!.paltabrain.event_schema.v1.EventB*\n&com.paltabrain.analytics.common.eventsP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.paltabrain.analytics.common.eventsP\001'
  _CONTEXTAPPLICATION._serialized_start=47
  _CONTEXTAPPLICATION._serialized_end=126
  _CONTEXTDEVICE._serialized_start=128
  _CONTEXTDEVICE._serialized_end=211
  _CONTEXTIDENTIFY._serialized_start=213
  _CONTEXTIDENTIFY._serialized_end=272
  _CONTEXTOS._serialized_start=274
  _CONTEXTOS._serialized_end=322
  _CONTEXTAPPSFLYER._serialized_start=324
  _CONTEXTAPPSFLYER._serialized_end=396
  _CONTEXTUSER._serialized_start=398
  _CONTEXTUSER._serialized_end=428
  _CONTEXT._serialized_start=431
  _CONTEXT._serialized_end=802
  _EVENTHEADERPARENT._serialized_start=804
  _EVENTHEADERPARENT._serialized_end=848
  _EVENTHEADER._serialized_start=850
  _EVENTHEADER._serialized_end=926
  _EVENTPAYLOADSESSIONSTART._serialized_start=928
  _EVENTPAYLOADSESSIONSTART._serialized_end=954
  _EVENTPAYLOADONBOARDINGSTART._serialized_start=956
  _EVENTPAYLOADONBOARDINGSTART._serialized_end=985
  _EVENTPAYLOADONBOARDINGFINISH._serialized_start=987
  _EVENTPAYLOADONBOARDINGFINISH._serialized_end=1017
  _EVENTPAYLOADPAGEOPEN._serialized_start=1019
  _EVENTPAYLOADPAGEOPEN._serialized_end=1058
  _EVENTPAYLOADPERMISSIONSREQUEST._serialized_start=1060
  _EVENTPAYLOADPERMISSIONSREQUEST._serialized_end=1126
  _EVENTPAYLOADEDGECASE._serialized_start=1129
  _EVENTPAYLOADEDGECASE._serialized_end=1627
  _EVENTCOMMON._serialized_start=1629
  _EVENTCOMMON._serialized_end=1731
  _EVENTPAYLOAD._serialized_start=1734
  _EVENTPAYLOAD._serialized_end=2205
  _EVENT._serialized_start=2208
  _EVENT._serialized_end=2388
  _BATCHCOMMON._serialized_start=2390
  _BATCHCOMMON._serialized_end=2500
  _BATCH._serialized_start=2503
  _BATCH._serialized_end=2672
# @@protoc_insertion_point(module_scope)
