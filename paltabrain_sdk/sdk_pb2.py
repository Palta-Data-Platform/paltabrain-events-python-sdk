# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdk.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsdk.proto\x12\x1bpaltabrain.event_schema.sdk\"\x85\x01\n\x0b\x45ventCommon\x12\x10\n\x08\x65vent_ts\x18\x01 \x01(\x12\x12\x17\n\nsession_id\x18\x02 \x01(\x12H\x00\x88\x01\x01\x12\"\n\x15session_event_seq_num\x18\x03 \x01(\x12H\x01\x88\x01\x01\x42\r\n\x0b_session_idB\x18\n\x16_session_event_seq_num\"b\n\x05\x45vent\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.paltabrain.event_schema.sdk.EventCommon\x12\x0e\n\x06header\x18\x02 \x01(\x0c\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\xa8\x01\n\x0b\x42\x61tchCommon\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61tch_id\x18\x02 \x01(\t\x12\x19\n\x0c\x63ountry_code\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06locale\x18\x04 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nutc_offset\x18\x05 \x01(\x12H\x02\x88\x01\x01\x42\x0f\n\r_country_codeB\t\n\x07_localeB\r\n\x0b_utc_offset\"\xc0\x03\n\x0e\x42\x61tchTelemetry\x12\x1b\n\x0e\x65vents_dropped\x18\x01 \x01(\x12H\x00\x88\x01\x01\x12\"\n\x15prev_connection_speed\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11prev_request_time\x18\x03 \x01(\x12H\x02\x88\x01\x01\x12#\n\x16\x65vents_reporting_speed\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1c\n\x14serialization_errors\x18\x05 \x03(\t\x12\x16\n\x0estorage_errors\x18\x06 \x03(\t\x12\x19\n\x0cstorage_used\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x19\n\x0ctrigger_type\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\"\n\x15time_since_last_batch\x18\t \x01(\x12H\x06\x88\x01\x01\x42\x11\n\x0f_events_droppedB\x18\n\x16_prev_connection_speedB\x14\n\x12_prev_request_timeB\x19\n\x17_events_reporting_speedB\x0f\n\r_storage_usedB\x0f\n\r_trigger_typeB\x18\n\x16_time_since_last_batch\"\xc6\x01\n\x05\x42\x61tch\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.paltabrain.event_schema.sdk.BatchCommon\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\x0c\x12\x32\n\x06\x65vents\x18\x03 \x03(\x0b\x32\".paltabrain.event_schema.sdk.Event\x12>\n\ttelemetry\x18\x04 \x01(\x0b\x32+.paltabrain.event_schema.sdk.BatchTelemetryb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sdk_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENTCOMMON._serialized_start=43
  _EVENTCOMMON._serialized_end=176
  _EVENT._serialized_start=178
  _EVENT._serialized_end=276
  _BATCHCOMMON._serialized_start=279
  _BATCHCOMMON._serialized_end=447
  _BATCHTELEMETRY._serialized_start=450
  _BATCHTELEMETRY._serialized_end=898
  _BATCH._serialized_start=901
  _BATCH._serialized_end=1099
# @@protoc_insertion_point(module_scope)
