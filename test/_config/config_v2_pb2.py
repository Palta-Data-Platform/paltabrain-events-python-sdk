# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_v2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63onfig_v2.proto\x12\x1apaltabrain.event_schema.v2\"\x8a\x01\n\x12\x43ontextApplication\x12\x13\n\x06\x61pp_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x61pp_version\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0c\x61pp_platform\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\t\n\x07_app_idB\x0e\n\x0c_app_versionB\x0f\n\r_app_platform\"\x97\x01\n\rContextDevice\x12\x19\n\x0c\x64\x65vice_brand\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0c\x64\x65vice_model\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0e\x64\x65vice_carrier\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0f\n\r_device_brandB\x0f\n\r_device_modelB\x11\n\x0f_device_carrier\"e\n\x0f\x43ontextIdentify\x12\x11\n\x04idfa\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04idfv\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04gaid\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_idfaB\x07\n\x05_idfvB\x07\n\x05_gaid\"U\n\tContextOs\x12\x14\n\x07os_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nos_version\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_os_nameB\r\n\x0b_os_version\"~\n\x10\x43ontextAppsflyer\x12\x19\n\x0c\x61ppsflyer_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12#\n\x16\x61ppsflyer_media_source\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0f\n\r_appsflyer_idB\x19\n\x17_appsflyer_media_source\"/\n\x0b\x43ontextUser\x12\x14\n\x07user_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_user_id\"\xf3\x02\n\x07\x43ontext\x12\x43\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32..paltabrain.event_schema.v2.ContextApplication\x12\x39\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32).paltabrain.event_schema.v2.ContextDevice\x12=\n\x08identify\x18\x03 \x01(\x0b\x32+.paltabrain.event_schema.v2.ContextIdentify\x12\x31\n\x02os\x18\x04 \x01(\x0b\x32%.paltabrain.event_schema.v2.ContextOs\x12?\n\tappsflyer\x18\x05 \x01(\x0b\x32,.paltabrain.event_schema.v2.ContextAppsflyer\x12\x35\n\x04user\x18\x06 \x01(\x0b\x32\'.paltabrain.event_schema.v2.ContextUser\",\n\x11\x45ventHeaderParent\x12\x17\n\x0fparent_elements\x18\x01 \x03(\t\"}\n\x15\x45ventHeaderOnboarding\x12\x1a\n\ronboarding_id\x18\x01 \x01(\x12H\x00\x88\x01\x01\x12\x1f\n\x12onboarding_version\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_onboarding_idB\x15\n\x13_onboarding_version\"\xff\x03\n\x13\x45ventHeaderEdgeCase\x12\x19\n\x0cprop_boolean\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x1b\n\x0eprop_decimal_1\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0eprop_decimal_2\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tprop_enum\x18\x04 \x01(\x12H\x03\x88\x01\x01\x12\x19\n\x0cprop_integer\x18\x05 \x01(\x12H\x04\x88\x01\x01\x12\x18\n\x0bprop_string\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1b\n\x0eprop_timestamp\x18\x07 \x01(\x12H\x06\x88\x01\x01\x12\x1a\n\x12prop_integer_array\x18\x08 \x03(\x12\x12]\n\x10prop_integer_map\x18\t \x03(\x0b\x32\x43.paltabrain.event_schema.v2.EventHeaderEdgeCase.PropIntegerMapEntry\x1a\x35\n\x13PropIntegerMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x42\x0f\n\r_prop_booleanB\x11\n\x0f_prop_decimal_1B\x11\n\x0f_prop_decimal_2B\x0c\n\n_prop_enumB\x0f\n\r_prop_integerB\x0e\n\x0c_prop_stringB\x11\n\x0f_prop_timestamp\"\xd7\x01\n\x0b\x45ventHeader\x12=\n\x06parent\x18\x01 \x01(\x0b\x32-.paltabrain.event_schema.v2.EventHeaderParent\x12\x45\n\nonboarding\x18\x02 \x01(\x0b\x32\x31.paltabrain.event_schema.v2.EventHeaderOnboarding\x12\x42\n\tedge_case\x18\x03 \x01(\x0b\x32/.paltabrain.event_schema.v2.EventHeaderEdgeCase\"\x1a\n\x18\x45ventPayloadSessionStart\"\x1d\n\x1b\x45ventPayloadOnboardingStart\"\x1e\n\x1c\x45ventPayloadOnboardingFinish\"8\n\x14\x45ventPayloadPageOpen\x12\x14\n\x07page_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_page_id\"d\n\x1e\x45ventPayloadPermissionsRequest\x12\x17\n\nis_granted\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x11\n\x04type\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\r\n\x0b_is_grantedB\x07\n\x05_type\"\xd8\x0b\n\x14\x45ventPayloadEdgeCase\x12\x19\n\x0cprop_boolean\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x1b\n\x0eprop_decimal_1\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0eprop_decimal_2\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tprop_enum\x18\x04 \x01(\x12H\x03\x88\x01\x01\x12\x19\n\x0cprop_integer\x18\x05 \x01(\x12H\x04\x88\x01\x01\x12\x18\n\x0bprop_string\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x1b\n\x0eprop_timestamp\x18\x07 \x01(\x12H\x06\x88\x01\x01\x12\x1a\n\x12prop_boolean_array\x18\x08 \x03(\x08\x12\x1a\n\x12prop_decimal_array\x18\t \x03(\t\x12\x17\n\x0fprop_enum_array\x18\n \x03(\x12\x12\x1a\n\x12prop_integer_array\x18\x0b \x03(\x12\x12\x19\n\x11prop_string_array\x18\x0c \x03(\t\x12\x1c\n\x14prop_timestamp_array\x18\r \x03(\x12\x12^\n\x10prop_boolean_map\x18\x0e \x03(\x0b\x32\x44.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropBooleanMapEntry\x12^\n\x10prop_decimal_map\x18\x0f \x03(\x0b\x32\x44.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropDecimalMapEntry\x12X\n\rprop_enum_map\x18\x10 \x03(\x0b\x32\x41.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropEnumMapEntry\x12^\n\x10prop_integer_map\x18\x11 \x03(\x0b\x32\x44.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropIntegerMapEntry\x12\\\n\x0fprop_string_map\x18\x12 \x03(\x0b\x32\x43.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropStringMapEntry\x12\x62\n\x12prop_timestamp_map\x18\x13 \x03(\x0b\x32\x46.paltabrain.event_schema.v2.EventPayloadEdgeCase.PropTimestampMapEntry\x12\x1b\n\x0eprop_decimal_3\x18\x14 \x01(\tH\x07\x88\x01\x01\x12\x1b\n\x0eprop_decimal_4\x18\x15 \x01(\tH\x08\x88\x01\x01\x1a\x35\n\x13PropBooleanMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a\x35\n\x13PropDecimalMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10PropEnumMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x35\n\x13PropIntegerMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x1a\x34\n\x12PropStringMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15PropTimestampMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\x42\x0f\n\r_prop_booleanB\x11\n\x0f_prop_decimal_1B\x11\n\x0f_prop_decimal_2B\x0c\n\n_prop_enumB\x0f\n\r_prop_integerB\x0e\n\x0c_prop_stringB\x11\n\x0f_prop_timestampB\x11\n\x0f_prop_decimal_3B\x11\n\x0f_prop_decimal_4\"\x81\x02\n\x19\x45ventPayloadBrandNewEvent\x12\x15\n\x08\x62rand_id\x18\x01 \x01(\x12H\x00\x88\x01\x01\x12\x17\n\nbrand_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nbrand_type\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04\x66rom\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05\x63lass\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05table\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x10\n\x03str\x18\x07 \x01(\tH\x06\x88\x01\x01\x42\x0b\n\t_brand_idB\r\n\x0b_brand_nameB\r\n\x0b_brand_typeB\x07\n\x05_fromB\x08\n\x06_classB\x08\n\x06_tableB\x06\n\x04_str\"6\n\x14\x45ventPayloadTestCase\x12\x13\n\x06test_1\x18\x01 \x01(\x12H\x00\x88\x01\x01\x42\t\n\x07_test_1\"\x1d\n\x1b\x45ventPayloadEmptyParamEvent\"5\n\x19\x45ventPayloadStrParamEvent\x12\x10\n\x03str\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x06\n\x04_str\"8\n\x1a\x45ventPayloadBoolParamEvent\x12\x11\n\x04\x62ool\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x07\n\x05_bool\"5\n\x19\x45ventPayloadIntParamEvent\x12\x10\n\x03int\x18\x01 \x01(\x12H\x00\x88\x01\x01\x42\x06\n\x04_int\"G\n\x1f\x45ventPayloadTimestampParamEvent\x12\x16\n\ttimestamp\x18\x01 \x01(\x12H\x00\x88\x01\x01\x42\x0c\n\n_timestamp\"A\n\x1d\x45ventPayloadDecimalParamEvent\x12\x14\n\x07\x64\x65\x63imal\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_decimal\"6\n\x1a\x45ventPayloadEnumParamEvent\x12\x10\n\x03int\x18\x01 \x01(\x12H\x00\x88\x01\x01\x42\x06\n\x04_int\".\n\x19\x45ventPayloadBoolListEvent\x12\x11\n\tbool_list\x18\x01 \x03(\x08\"4\n\x1c\x45ventPayloadDecimalListEvent\x12\x14\n\x0c\x64\x65\x63imal_list\x18\x01 \x03(\t\".\n\x19\x45ventPayloadEnumListEvent\x12\x11\n\tenum_list\x18\x01 \x03(\x12\",\n\x18\x45ventPayloadIntListEvent\x12\x10\n\x08int_list\x18\x01 \x03(\x12\",\n\x18\x45ventPayloadStrListEvent\x12\x10\n\x08str_list\x18\x01 \x03(\t\"8\n\x1e\x45ventPayloadTimestampListEvent\x12\x16\n\x0etimestamp_list\x18\x01 \x03(\x12\"\x9f\x01\n\x18\x45ventPayloadBoolMapEvent\x12S\n\x08\x62ool_map\x18\x01 \x03(\x0b\x32\x41.paltabrain.event_schema.v2.EventPayloadBoolMapEvent.BoolMapEntry\x1a.\n\x0c\x42oolMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\xae\x01\n\x1b\x45ventPayloadDecimalMapEvent\x12\\\n\x0b\x64\x65\x63imal_map\x18\x01 \x03(\x0b\x32G.paltabrain.event_schema.v2.EventPayloadDecimalMapEvent.DecimalMapEntry\x1a\x31\n\x0f\x44\x65\x63imalMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x01\n\x18\x45ventPayloadEnumMapEvent\x12S\n\x08\x65num_map\x18\x01 \x03(\x0b\x32\x41.paltabrain.event_schema.v2.EventPayloadEnumMapEvent.EnumMapEntry\x1a.\n\x0c\x45numMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\"\x9a\x01\n\x17\x45ventPayloadIntMapEvent\x12P\n\x07int_map\x18\x01 \x03(\x0b\x32?.paltabrain.event_schema.v2.EventPayloadIntMapEvent.IntMapEntry\x1a-\n\x0bIntMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\"\x9a\x01\n\x17\x45ventPayloadStrMapEvent\x12P\n\x07str_map\x18\x01 \x03(\x0b\x32?.paltabrain.event_schema.v2.EventPayloadStrMapEvent.StrMapEntry\x1a-\n\x0bStrMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb8\x01\n\x1d\x45ventPayloadTimestampMapEvent\x12\x62\n\rtimestamp_map\x18\x01 \x03(\x0b\x32K.paltabrain.event_schema.v2.EventPayloadTimestampMapEvent.TimestampMapEntry\x1a\x33\n\x11TimestampMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x12:\x02\x38\x01\"\x1d\n\x1b\x45ventPayloadDeprecatedEvent\"\xa1\x01\n#EventPayloadDeprecatedPropertyEvent\x12 \n\x13\x64\x65precated_property\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12$\n\x17not_deprecated_property\x18\x02 \x01(\x08H\x01\x88\x01\x01\x42\x16\n\x14_deprecated_propertyB\x1a\n\x18_not_deprecated_property\"\xcc\x06\n\x1e\x45ventPayloadKotlinKeywordEvent\x12\x0f\n\x02\x61s\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\x05\x62reak\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x12\n\x05\x63lass\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x15\n\x08\x63ontinue\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x0f\n\x02\x64o\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x11\n\x04\x65lse\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x12\n\x05\x66\x61lse\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x10\n\x03\x66or\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x10\n\x03\x66un\x18\t \x01(\x08H\x08\x88\x01\x01\x12\x0f\n\x02if\x18\n \x01(\x08H\t\x88\x01\x01\x12\x0f\n\x02in\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x16\n\tinterface\x18\x0c \x01(\x08H\x0b\x88\x01\x01\x12\x0f\n\x02is\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\x11\n\x04null\x18\x0e \x01(\x08H\r\x88\x01\x01\x12\x13\n\x06object\x18\x0f \x01(\x08H\x0e\x88\x01\x01\x12\x14\n\x07package\x18\x10 \x01(\x08H\x0f\x88\x01\x01\x12\x13\n\x06return\x18\x11 \x01(\x08H\x10\x88\x01\x01\x12\x12\n\x05super\x18\x12 \x01(\x08H\x11\x88\x01\x01\x12\x11\n\x04this\x18\x13 \x01(\x08H\x12\x88\x01\x01\x12\x12\n\x05throw\x18\x14 \x01(\x08H\x13\x88\x01\x01\x12\x11\n\x04true\x18\x15 \x01(\x08H\x14\x88\x01\x01\x12\x16\n\ttypealias\x18\x16 \x01(\x08H\x15\x88\x01\x01\x12\x13\n\x06typeof\x18\x17 \x01(\x08H\x16\x88\x01\x01\x12\x10\n\x03try\x18\x18 \x01(\x08H\x17\x88\x01\x01\x12\x10\n\x03val\x18\x19 \x01(\x08H\x18\x88\x01\x01\x12\x10\n\x03var\x18\x1a \x01(\x08H\x19\x88\x01\x01\x12\x12\n\x05while\x18\x1b \x01(\x08H\x1a\x88\x01\x01\x12\x11\n\x04when\x18\x1c \x01(\x08H\x1b\x88\x01\x01\x42\x05\n\x03_asB\x08\n\x06_breakB\x08\n\x06_classB\x0b\n\t_continueB\x05\n\x03_doB\x07\n\x05_elseB\x08\n\x06_falseB\x06\n\x04_forB\x06\n\x04_funB\x05\n\x03_ifB\x05\n\x03_inB\x0c\n\n_interfaceB\x05\n\x03_isB\x07\n\x05_nullB\t\n\x07_objectB\n\n\x08_packageB\t\n\x07_returnB\x08\n\x06_superB\x07\n\x05_thisB\x08\n\x06_throwB\x07\n\x05_trueB\x0c\n\n_typealiasB\t\n\x07_typeofB\x06\n\x04_tryB\x06\n\x04_valB\x06\n\x04_varB\x08\n\x06_whileB\x07\n\x05_when\"\xac\x0b\n\"EventPayloadJavascriptKeywordEvent\x12\x12\n\x05\x61wait\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\x05\x62reak\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x11\n\x04\x63\x61se\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x12\n\x05\x63\x61tch\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x12\n\x05\x63lass\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x12\n\x05\x63onst\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x15\n\x08\x63ontinue\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08\x64\x65\x62ugger\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x14\n\x07\x64\x65\x66\x61ult\x18\t \x01(\x08H\x08\x88\x01\x01\x12\x13\n\x06\x64\x65lete\x18\n \x01(\x08H\t\x88\x01\x01\x12\x0f\n\x02\x64o\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x11\n\x04\x65lse\x18\x0c \x01(\x08H\x0b\x88\x01\x01\x12\x11\n\x04\x65num\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\x13\n\x06\x65xport\x18\x0e \x01(\x08H\r\x88\x01\x01\x12\x14\n\x07\x65xtends\x18\x0f \x01(\x08H\x0e\x88\x01\x01\x12\x12\n\x05\x66\x61lse\x18\x10 \x01(\x08H\x0f\x88\x01\x01\x12\x14\n\x07\x66inally\x18\x11 \x01(\x08H\x10\x88\x01\x01\x12\x10\n\x03\x66or\x18\x12 \x01(\x08H\x11\x88\x01\x01\x12\x15\n\x08\x66unction\x18\x13 \x01(\x08H\x12\x88\x01\x01\x12\x0f\n\x02if\x18\x14 \x01(\x08H\x13\x88\x01\x01\x12\x17\n\nimplements\x18\x15 \x01(\x08H\x14\x88\x01\x01\x12\x13\n\x06import\x18\x16 \x01(\x08H\x15\x88\x01\x01\x12\x0f\n\x02in\x18\x17 \x01(\x08H\x16\x88\x01\x01\x12\x17\n\ninstanceof\x18\x18 \x01(\x08H\x17\x88\x01\x01\x12\x16\n\tinterface\x18\x19 \x01(\x08H\x18\x88\x01\x01\x12\x10\n\x03let\x18\x1a \x01(\x08H\x19\x88\x01\x01\x12\x10\n\x03new\x18\x1b \x01(\x08H\x1a\x88\x01\x01\x12\x11\n\x04null\x18\x1c \x01(\x08H\x1b\x88\x01\x01\x12\x14\n\x07package\x18\x1d \x01(\x08H\x1c\x88\x01\x01\x12\x14\n\x07private\x18\x1e \x01(\x08H\x1d\x88\x01\x01\x12\x16\n\tprotected\x18\x1f \x01(\x08H\x1e\x88\x01\x01\x12\x13\n\x06public\x18  \x01(\x08H\x1f\x88\x01\x01\x12\x13\n\x06return\x18! \x01(\x08H \x88\x01\x01\x12\x12\n\x05super\x18\" \x01(\x08H!\x88\x01\x01\x12\x13\n\x06switch\x18# \x01(\x08H\"\x88\x01\x01\x12\x13\n\x06static\x18$ \x01(\x08H#\x88\x01\x01\x12\x11\n\x04this\x18% \x01(\x08H$\x88\x01\x01\x12\x12\n\x05throw\x18& \x01(\x08H%\x88\x01\x01\x12\x10\n\x03try\x18\' \x01(\x08H&\x88\x01\x01\x12\x11\n\x04true\x18( \x01(\x08H\'\x88\x01\x01\x12\x13\n\x06typeof\x18) \x01(\x08H(\x88\x01\x01\x12\x10\n\x03var\x18* \x01(\x08H)\x88\x01\x01\x12\x11\n\x04void\x18+ \x01(\x08H*\x88\x01\x01\x12\x12\n\x05while\x18, \x01(\x08H+\x88\x01\x01\x12\x11\n\x04with\x18- \x01(\x08H,\x88\x01\x01\x12\x12\n\x05yield\x18. \x01(\x08H-\x88\x01\x01\x42\x08\n\x06_awaitB\x08\n\x06_breakB\x07\n\x05_caseB\x08\n\x06_catchB\x08\n\x06_classB\x08\n\x06_constB\x0b\n\t_continueB\x0b\n\t_debuggerB\n\n\x08_defaultB\t\n\x07_deleteB\x05\n\x03_doB\x07\n\x05_elseB\x07\n\x05_enumB\t\n\x07_exportB\n\n\x08_extendsB\x08\n\x06_falseB\n\n\x08_finallyB\x06\n\x04_forB\x0b\n\t_functionB\x05\n\x03_ifB\r\n\x0b_implementsB\t\n\x07_importB\x05\n\x03_inB\r\n\x0b_instanceofB\x0c\n\n_interfaceB\x06\n\x04_letB\x06\n\x04_newB\x07\n\x05_nullB\n\n\x08_packageB\n\n\x08_privateB\x0c\n\n_protectedB\t\n\x07_publicB\t\n\x07_returnB\x08\n\x06_superB\t\n\x07_switchB\t\n\x07_staticB\x07\n\x05_thisB\x08\n\x06_throwB\x06\n\x04_tryB\x07\n\x05_trueB\t\n\x07_typeofB\x06\n\x04_varB\x07\n\x05_voidB\x08\n\x06_whileB\x07\n\x05_withB\x08\n\x06_yield\"\x87\x10\n\x1d\x45ventPayloadSwiftKeywordEvent\x12\x12\n\x05\x63lass\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x06\x64\x65init\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x11\n\x04\x65num\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x16\n\textension\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x11\n\x04\x66unc\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x13\n\x06import\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x11\n\x04init\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08operator\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x14\n\x07private\x18\t \x01(\x08H\x08\x88\x01\x01\x12\x15\n\x08protocol\x18\n \x01(\x08H\t\x88\x01\x01\x12\x13\n\x06public\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x13\n\x06static\x18\x0c \x01(\x08H\x0b\x88\x01\x01\x12\x13\n\x06struct\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\x16\n\tsubscript\x18\x0e \x01(\x08H\r\x88\x01\x01\x12\x12\n\x05\x62reak\x18\x0f \x01(\x08H\x0e\x88\x01\x01\x12\x11\n\x04\x63\x61se\x18\x10 \x01(\x08H\x0f\x88\x01\x01\x12\x15\n\x08\x63ontinue\x18\x11 \x01(\x08H\x10\x88\x01\x01\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x12 \x01(\x08H\x11\x88\x01\x01\x12\x0f\n\x02\x64o\x18\x13 \x01(\x08H\x12\x88\x01\x01\x12\x11\n\x04\x65lse\x18\x14 \x01(\x08H\x13\x88\x01\x01\x12\x10\n\x03\x66or\x18\x15 \x01(\x08H\x14\x88\x01\x01\x12\x13\n\x06return\x18\x16 \x01(\x08H\x15\x88\x01\x01\x12\x13\n\x06switch\x18\x17 \x01(\x08H\x16\x88\x01\x01\x12\x12\n\x05where\x18\x18 \x01(\x08H\x17\x88\x01\x01\x12\x12\n\x05while\x18\x19 \x01(\x08H\x18\x88\x01\x01\x12\x0f\n\x02\x61s\x18\x1a \x01(\x08H\x19\x88\x01\x01\x12\x12\n\x05\x66\x61lse\x18\x1b \x01(\x08H\x1a\x88\x01\x01\x12\x0f\n\x02is\x18\x1c \x01(\x08H\x1b\x88\x01\x01\x12\x19\n\x0c\x64ynamic_type\x18\x1d \x01(\x08H\x1c\x88\x01\x01\x12\x12\n\x05super\x18\x1e \x01(\x08H\x1d\x88\x01\x01\x12\x11\n\x04true\x18\x1f \x01(\x08H\x1e\x88\x01\x01\x12\x10\n\x03let\x18  \x01(\x08H\x1f\x88\x01\x01\x12\x0f\n\x02in\x18! \x01(\x08H \x88\x01\x01\x12\x15\n\x08internal\x18\" \x01(\x08H!\x88\x01\x01\x12\x16\n\ttypealias\x18# \x01(\x08H\"\x88\x01\x01\x12\x0f\n\x02if\x18$ \x01(\x08H#\x88\x01\x01\x12\x10\n\x03nil\x18% \x01(\x08H$\x88\x01\x01\x12\x10\n\x03var\x18& \x01(\x08H%\x88\x01\x01\x12\x11\n\x04self\x18\' \x01(\x08H&\x88\x01\x01\x12\x14\n\x07unowned\x18( \x01(\x08H\'\x88\x01\x01\x12\x1a\n\rassociativity\x18) \x01(\x08H(\x88\x01\x01\x12\x18\n\x0b\x63onvenience\x18* \x01(\x08H)\x88\x01\x01\x12\x14\n\x07\x64ynamic\x18+ \x01(\x08H*\x88\x01\x01\x12\x14\n\x07\x64id_set\x18, \x01(\x08H+\x88\x01\x01\x12\x17\n\nprecedence\x18- \x01(\x08H,\x88\x01\x01\x12\x12\n\x05\x66inal\x18. \x01(\x08H-\x88\x01\x01\x12\x10\n\x03get\x18/ \x01(\x08H.\x88\x01\x01\x12\x12\n\x05infix\x18\x30 \x01(\x08H/\x88\x01\x01\x12\x12\n\x05inout\x18\x31 \x01(\x08H0\x88\x01\x01\x12\x12\n\x05right\x18\x32 \x01(\x08H1\x88\x01\x01\x12\x10\n\x03set\x18\x33 \x01(\x08H2\x88\x01\x01\x12\x11\n\x04type\x18\x34 \x01(\x08H3\x88\x01\x01\x12\x11\n\x04lazy\x18\x35 \x01(\x08H4\x88\x01\x01\x12\x11\n\x04left\x18\x36 \x01(\x08H5\x88\x01\x01\x12\x15\n\x08mutating\x18\x37 \x01(\x08H6\x88\x01\x01\x12\x11\n\x04none\x18\x38 \x01(\x08H7\x88\x01\x01\x12\x11\n\x04weak\x18\x39 \x01(\x08H8\x88\x01\x01\x12\x15\n\x08will_set\x18: \x01(\x08H9\x88\x01\x01\x12\x13\n\x06prefix\x18; \x01(\x08H:\x88\x01\x01\x12\x18\n\x0bnonmutating\x18< \x01(\x08H;\x88\x01\x01\x12\x15\n\x08optional\x18= \x01(\x08H<\x88\x01\x01\x12\x15\n\x08override\x18> \x01(\x08H=\x88\x01\x01\x12\x14\n\x07postfix\x18? \x01(\x08H>\x88\x01\x01\x12\x15\n\x08required\x18@ \x01(\x08H?\x88\x01\x01\x42\x08\n\x06_classB\t\n\x07_deinitB\x07\n\x05_enumB\x0c\n\n_extensionB\x07\n\x05_funcB\t\n\x07_importB\x07\n\x05_initB\x0b\n\t_operatorB\n\n\x08_privateB\x0b\n\t_protocolB\t\n\x07_publicB\t\n\x07_staticB\t\n\x07_structB\x0c\n\n_subscriptB\x08\n\x06_breakB\x07\n\x05_caseB\x0b\n\t_continueB\n\n\x08_defaultB\x05\n\x03_doB\x07\n\x05_elseB\x06\n\x04_forB\t\n\x07_returnB\t\n\x07_switchB\x08\n\x06_whereB\x08\n\x06_whileB\x05\n\x03_asB\x08\n\x06_falseB\x05\n\x03_isB\x0f\n\r_dynamic_typeB\x08\n\x06_superB\x07\n\x05_trueB\x06\n\x04_letB\x05\n\x03_inB\x0b\n\t_internalB\x0c\n\n_typealiasB\x05\n\x03_ifB\x06\n\x04_nilB\x06\n\x04_varB\x07\n\x05_selfB\n\n\x08_unownedB\x10\n\x0e_associativityB\x0e\n\x0c_convenienceB\n\n\x08_dynamicB\n\n\x08_did_setB\r\n\x0b_precedenceB\x08\n\x06_finalB\x06\n\x04_getB\x08\n\x06_infixB\x08\n\x06_inoutB\x08\n\x06_rightB\x06\n\x04_setB\x07\n\x05_typeB\x07\n\x05_lazyB\x07\n\x05_leftB\x0b\n\t_mutatingB\x07\n\x05_noneB\x07\n\x05_weakB\x0b\n\t_will_setB\t\n\x07_prefixB\x0e\n\x0c_nonmutatingB\x0b\n\t_optionalB\x0b\n\t_overrideB\n\n\x08_postfixB\x0b\n\t_required\"\xbc\x07\n\x1e\x45ventPayloadPythonKeywordEvent\x12\x12\n\x05\x61wait\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x11\n\x04\x65lse\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x06import\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x04pass\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x12\n\x05\x62reak\x18\x05 \x01(\x08H\x04\x88\x01\x01\x12\x13\n\x06\x65xcept\x18\x06 \x01(\x08H\x05\x88\x01\x01\x12\x0f\n\x02in\x18\x07 \x01(\x08H\x06\x88\x01\x01\x12\x12\n\x05raise\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x12\n\x05\x63lass\x18\t \x01(\x08H\x08\x88\x01\x01\x12\x14\n\x07\x66inally\x18\n \x01(\x08H\t\x88\x01\x01\x12\x0f\n\x02is\x18\x0b \x01(\x08H\n\x88\x01\x01\x12\x13\n\x06return\x18\x0c \x01(\x08H\x0b\x88\x01\x01\x12\x10\n\x03\x61nd\x18\r \x01(\x08H\x0c\x88\x01\x01\x12\x15\n\x08\x63ontinue\x18\x0e \x01(\x08H\r\x88\x01\x01\x12\x10\n\x03\x66or\x18\x0f \x01(\x08H\x0e\x88\x01\x01\x12\x13\n\x06lambda\x18\x10 \x01(\x08H\x0f\x88\x01\x01\x12\x10\n\x03try\x18\x11 \x01(\x08H\x10\x88\x01\x01\x12\x0f\n\x02\x61s\x18\x12 \x01(\x08H\x11\x88\x01\x01\x12\x10\n\x03\x64\x65\x66\x18\x13 \x01(\x08H\x12\x88\x01\x01\x12\x11\n\x04\x66rom\x18\x14 \x01(\x08H\x13\x88\x01\x01\x12\x15\n\x08nonlocal\x18\x15 \x01(\x08H\x14\x88\x01\x01\x12\x12\n\x05while\x18\x16 \x01(\x08H\x15\x88\x01\x01\x12\x13\n\x06\x61ssert\x18\x17 \x01(\x08H\x16\x88\x01\x01\x12\x10\n\x03\x64\x65l\x18\x18 \x01(\x08H\x17\x88\x01\x01\x12\x13\n\x06global\x18\x19 \x01(\x08H\x18\x88\x01\x01\x12\x10\n\x03not\x18\x1a \x01(\x08H\x19\x88\x01\x01\x12\x11\n\x04with\x18\x1b \x01(\x08H\x1a\x88\x01\x01\x12\x12\n\x05\x61sync\x18\x1c \x01(\x08H\x1b\x88\x01\x01\x12\x11\n\x04\x65lif\x18\x1d \x01(\x08H\x1c\x88\x01\x01\x12\x0f\n\x02if\x18\x1e \x01(\x08H\x1d\x88\x01\x01\x12\x0f\n\x02or\x18\x1f \x01(\x08H\x1e\x88\x01\x01\x12\x12\n\x05yield\x18  \x01(\x08H\x1f\x88\x01\x01\x42\x08\n\x06_awaitB\x07\n\x05_elseB\t\n\x07_importB\x07\n\x05_passB\x08\n\x06_breakB\t\n\x07_exceptB\x05\n\x03_inB\x08\n\x06_raiseB\x08\n\x06_classB\n\n\x08_finallyB\x05\n\x03_isB\t\n\x07_returnB\x06\n\x04_andB\x0b\n\t_continueB\x06\n\x04_forB\t\n\x07_lambdaB\x06\n\x04_tryB\x05\n\x03_asB\x06\n\x04_defB\x07\n\x05_fromB\x0b\n\t_nonlocalB\x08\n\x06_whileB\t\n\x07_assertB\x06\n\x04_delB\t\n\x07_globalB\x06\n\x04_notB\x07\n\x05_withB\x08\n\x06_asyncB\x07\n\x05_elifB\x05\n\x03_ifB\x05\n\x03_orB\x08\n\x06_yield\"r\n\x18\x45ventPayloadIosOnlyEvent\x12\x1a\n\rtest_property\x18\x01 \x01(\x12H\x00\x88\x01\x01\x12\x18\n\x0bstring_prop\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x10\n\x0e_test_propertyB\x0e\n\x0c_string_prop\"\xb9\x14\n\x0c\x45ventPayload\x12G\n\x07\x65vent_1\x18\x01 \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadSessionStartH\x00\x12J\n\x07\x65vent_2\x18\x02 \x01(\x0b\x32\x37.paltabrain.event_schema.v2.EventPayloadOnboardingStartH\x00\x12K\n\x07\x65vent_3\x18\x03 \x01(\x0b\x32\x38.paltabrain.event_schema.v2.EventPayloadOnboardingFinishH\x00\x12\x43\n\x07\x65vent_4\x18\x04 \x01(\x0b\x32\x30.paltabrain.event_schema.v2.EventPayloadPageOpenH\x00\x12M\n\x07\x65vent_5\x18\x05 \x01(\x0b\x32:.paltabrain.event_schema.v2.EventPayloadPermissionsRequestH\x00\x12\x43\n\x07\x65vent_6\x18\x06 \x01(\x0b\x32\x30.paltabrain.event_schema.v2.EventPayloadEdgeCaseH\x00\x12H\n\x07\x65vent_7\x18\x07 \x01(\x0b\x32\x35.paltabrain.event_schema.v2.EventPayloadBrandNewEventH\x00\x12\x43\n\x07\x65vent_8\x18\x08 \x01(\x0b\x32\x30.paltabrain.event_schema.v2.EventPayloadTestCaseH\x00\x12J\n\x07\x65vent_9\x18\t \x01(\x0b\x32\x37.paltabrain.event_schema.v2.EventPayloadEmptyParamEventH\x00\x12I\n\x08\x65vent_10\x18\n \x01(\x0b\x32\x35.paltabrain.event_schema.v2.EventPayloadStrParamEventH\x00\x12J\n\x08\x65vent_11\x18\x0b \x01(\x0b\x32\x36.paltabrain.event_schema.v2.EventPayloadBoolParamEventH\x00\x12I\n\x08\x65vent_12\x18\x0c \x01(\x0b\x32\x35.paltabrain.event_schema.v2.EventPayloadIntParamEventH\x00\x12O\n\x08\x65vent_13\x18\r \x01(\x0b\x32;.paltabrain.event_schema.v2.EventPayloadTimestampParamEventH\x00\x12M\n\x08\x65vent_14\x18\x0e \x01(\x0b\x32\x39.paltabrain.event_schema.v2.EventPayloadDecimalParamEventH\x00\x12J\n\x08\x65vent_15\x18\x0f \x01(\x0b\x32\x36.paltabrain.event_schema.v2.EventPayloadEnumParamEventH\x00\x12I\n\x08\x65vent_16\x18\x10 \x01(\x0b\x32\x35.paltabrain.event_schema.v2.EventPayloadBoolListEventH\x00\x12L\n\x08\x65vent_17\x18\x11 \x01(\x0b\x32\x38.paltabrain.event_schema.v2.EventPayloadDecimalListEventH\x00\x12I\n\x08\x65vent_18\x18\x12 \x01(\x0b\x32\x35.paltabrain.event_schema.v2.EventPayloadEnumListEventH\x00\x12H\n\x08\x65vent_19\x18\x13 \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadIntListEventH\x00\x12H\n\x08\x65vent_20\x18\x14 \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadStrListEventH\x00\x12N\n\x08\x65vent_21\x18\x15 \x01(\x0b\x32:.paltabrain.event_schema.v2.EventPayloadTimestampListEventH\x00\x12H\n\x08\x65vent_22\x18\x16 \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadBoolMapEventH\x00\x12K\n\x08\x65vent_23\x18\x17 \x01(\x0b\x32\x37.paltabrain.event_schema.v2.EventPayloadDecimalMapEventH\x00\x12H\n\x08\x65vent_24\x18\x18 \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadEnumMapEventH\x00\x12G\n\x08\x65vent_25\x18\x19 \x01(\x0b\x32\x33.paltabrain.event_schema.v2.EventPayloadIntMapEventH\x00\x12G\n\x08\x65vent_26\x18\x1a \x01(\x0b\x32\x33.paltabrain.event_schema.v2.EventPayloadStrMapEventH\x00\x12M\n\x08\x65vent_27\x18\x1b \x01(\x0b\x32\x39.paltabrain.event_schema.v2.EventPayloadTimestampMapEventH\x00\x12K\n\x08\x65vent_28\x18\x1c \x01(\x0b\x32\x37.paltabrain.event_schema.v2.EventPayloadDeprecatedEventH\x00\x12S\n\x08\x65vent_29\x18\x1d \x01(\x0b\x32?.paltabrain.event_schema.v2.EventPayloadDeprecatedPropertyEventH\x00\x12N\n\x08\x65vent_30\x18\x1e \x01(\x0b\x32:.paltabrain.event_schema.v2.EventPayloadKotlinKeywordEventH\x00\x12R\n\x08\x65vent_31\x18\x1f \x01(\x0b\x32>.paltabrain.event_schema.v2.EventPayloadJavascriptKeywordEventH\x00\x12M\n\x08\x65vent_32\x18  \x01(\x0b\x32\x39.paltabrain.event_schema.v2.EventPayloadSwiftKeywordEventH\x00\x12N\n\x08\x65vent_33\x18! \x01(\x0b\x32:.paltabrain.event_schema.v2.EventPayloadPythonKeywordEventH\x00\x12H\n\x08\x65vent_34\x18\" \x01(\x0b\x32\x34.paltabrain.event_schema.v2.EventPayloadIosOnlyEventH\x00\x42\x0c\n\nevent_typeB*\n&com.paltabrain.analytics.common.eventsP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_v2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.paltabrain.analytics.common.eventsP\001'
  _EVENTHEADEREDGECASE_PROPINTEGERMAPENTRY._options = None
  _EVENTHEADEREDGECASE_PROPINTEGERMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPBOOLEANMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPBOOLEANMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPDECIMALMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPDECIMALMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPENUMMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPENUMMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPINTEGERMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPINTEGERMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPSTRINGMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPSTRINGMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADEDGECASE_PROPTIMESTAMPMAPENTRY._options = None
  _EVENTPAYLOADEDGECASE_PROPTIMESTAMPMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADBOOLMAPEVENT_BOOLMAPENTRY._options = None
  _EVENTPAYLOADBOOLMAPEVENT_BOOLMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADDECIMALMAPEVENT_DECIMALMAPENTRY._options = None
  _EVENTPAYLOADDECIMALMAPEVENT_DECIMALMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADENUMMAPEVENT_ENUMMAPENTRY._options = None
  _EVENTPAYLOADENUMMAPEVENT_ENUMMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADINTMAPEVENT_INTMAPENTRY._options = None
  _EVENTPAYLOADINTMAPEVENT_INTMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADSTRMAPEVENT_STRMAPENTRY._options = None
  _EVENTPAYLOADSTRMAPEVENT_STRMAPENTRY._serialized_options = b'8\001'
  _EVENTPAYLOADTIMESTAMPMAPEVENT_TIMESTAMPMAPENTRY._options = None
  _EVENTPAYLOADTIMESTAMPMAPEVENT_TIMESTAMPMAPENTRY._serialized_options = b'8\001'
  _CONTEXTAPPLICATION._serialized_start=48
  _CONTEXTAPPLICATION._serialized_end=186
  _CONTEXTDEVICE._serialized_start=189
  _CONTEXTDEVICE._serialized_end=340
  _CONTEXTIDENTIFY._serialized_start=342
  _CONTEXTIDENTIFY._serialized_end=443
  _CONTEXTOS._serialized_start=445
  _CONTEXTOS._serialized_end=530
  _CONTEXTAPPSFLYER._serialized_start=532
  _CONTEXTAPPSFLYER._serialized_end=658
  _CONTEXTUSER._serialized_start=660
  _CONTEXTUSER._serialized_end=707
  _CONTEXT._serialized_start=710
  _CONTEXT._serialized_end=1081
  _EVENTHEADERPARENT._serialized_start=1083
  _EVENTHEADERPARENT._serialized_end=1127
  _EVENTHEADERONBOARDING._serialized_start=1129
  _EVENTHEADERONBOARDING._serialized_end=1254
  _EVENTHEADEREDGECASE._serialized_start=1257
  _EVENTHEADEREDGECASE._serialized_end=1768
  _EVENTHEADEREDGECASE_PROPINTEGERMAPENTRY._serialized_start=1594
  _EVENTHEADEREDGECASE_PROPINTEGERMAPENTRY._serialized_end=1647
  _EVENTHEADER._serialized_start=1771
  _EVENTHEADER._serialized_end=1986
  _EVENTPAYLOADSESSIONSTART._serialized_start=1988
  _EVENTPAYLOADSESSIONSTART._serialized_end=2014
  _EVENTPAYLOADONBOARDINGSTART._serialized_start=2016
  _EVENTPAYLOADONBOARDINGSTART._serialized_end=2045
  _EVENTPAYLOADONBOARDINGFINISH._serialized_start=2047
  _EVENTPAYLOADONBOARDINGFINISH._serialized_end=2077
  _EVENTPAYLOADPAGEOPEN._serialized_start=2079
  _EVENTPAYLOADPAGEOPEN._serialized_end=2135
  _EVENTPAYLOADPERMISSIONSREQUEST._serialized_start=2137
  _EVENTPAYLOADPERMISSIONSREQUEST._serialized_end=2237
  _EVENTPAYLOADEDGECASE._serialized_start=2240
  _EVENTPAYLOADEDGECASE._serialized_end=3736
  _EVENTPAYLOADEDGECASE_PROPBOOLEANMAPENTRY._serialized_start=3251
  _EVENTPAYLOADEDGECASE_PROPBOOLEANMAPENTRY._serialized_end=3304
  _EVENTPAYLOADEDGECASE_PROPDECIMALMAPENTRY._serialized_start=3306
  _EVENTPAYLOADEDGECASE_PROPDECIMALMAPENTRY._serialized_end=3359
  _EVENTPAYLOADEDGECASE_PROPENUMMAPENTRY._serialized_start=3361
  _EVENTPAYLOADEDGECASE_PROPENUMMAPENTRY._serialized_end=3411
  _EVENTPAYLOADEDGECASE_PROPINTEGERMAPENTRY._serialized_start=1594
  _EVENTPAYLOADEDGECASE_PROPINTEGERMAPENTRY._serialized_end=1647
  _EVENTPAYLOADEDGECASE_PROPSTRINGMAPENTRY._serialized_start=3468
  _EVENTPAYLOADEDGECASE_PROPSTRINGMAPENTRY._serialized_end=3520
  _EVENTPAYLOADEDGECASE_PROPTIMESTAMPMAPENTRY._serialized_start=3522
  _EVENTPAYLOADEDGECASE_PROPTIMESTAMPMAPENTRY._serialized_end=3577
  _EVENTPAYLOADBRANDNEWEVENT._serialized_start=3739
  _EVENTPAYLOADBRANDNEWEVENT._serialized_end=3996
  _EVENTPAYLOADTESTCASE._serialized_start=3998
  _EVENTPAYLOADTESTCASE._serialized_end=4052
  _EVENTPAYLOADEMPTYPARAMEVENT._serialized_start=4054
  _EVENTPAYLOADEMPTYPARAMEVENT._serialized_end=4083
  _EVENTPAYLOADSTRPARAMEVENT._serialized_start=4085
  _EVENTPAYLOADSTRPARAMEVENT._serialized_end=4138
  _EVENTPAYLOADBOOLPARAMEVENT._serialized_start=4140
  _EVENTPAYLOADBOOLPARAMEVENT._serialized_end=4196
  _EVENTPAYLOADINTPARAMEVENT._serialized_start=4198
  _EVENTPAYLOADINTPARAMEVENT._serialized_end=4251
  _EVENTPAYLOADTIMESTAMPPARAMEVENT._serialized_start=4253
  _EVENTPAYLOADTIMESTAMPPARAMEVENT._serialized_end=4324
  _EVENTPAYLOADDECIMALPARAMEVENT._serialized_start=4326
  _EVENTPAYLOADDECIMALPARAMEVENT._serialized_end=4391
  _EVENTPAYLOADENUMPARAMEVENT._serialized_start=4393
  _EVENTPAYLOADENUMPARAMEVENT._serialized_end=4447
  _EVENTPAYLOADBOOLLISTEVENT._serialized_start=4449
  _EVENTPAYLOADBOOLLISTEVENT._serialized_end=4495
  _EVENTPAYLOADDECIMALLISTEVENT._serialized_start=4497
  _EVENTPAYLOADDECIMALLISTEVENT._serialized_end=4549
  _EVENTPAYLOADENUMLISTEVENT._serialized_start=4551
  _EVENTPAYLOADENUMLISTEVENT._serialized_end=4597
  _EVENTPAYLOADINTLISTEVENT._serialized_start=4599
  _EVENTPAYLOADINTLISTEVENT._serialized_end=4643
  _EVENTPAYLOADSTRLISTEVENT._serialized_start=4645
  _EVENTPAYLOADSTRLISTEVENT._serialized_end=4689
  _EVENTPAYLOADTIMESTAMPLISTEVENT._serialized_start=4691
  _EVENTPAYLOADTIMESTAMPLISTEVENT._serialized_end=4747
  _EVENTPAYLOADBOOLMAPEVENT._serialized_start=4750
  _EVENTPAYLOADBOOLMAPEVENT._serialized_end=4909
  _EVENTPAYLOADBOOLMAPEVENT_BOOLMAPENTRY._serialized_start=4863
  _EVENTPAYLOADBOOLMAPEVENT_BOOLMAPENTRY._serialized_end=4909
  _EVENTPAYLOADDECIMALMAPEVENT._serialized_start=4912
  _EVENTPAYLOADDECIMALMAPEVENT._serialized_end=5086
  _EVENTPAYLOADDECIMALMAPEVENT_DECIMALMAPENTRY._serialized_start=5037
  _EVENTPAYLOADDECIMALMAPEVENT_DECIMALMAPENTRY._serialized_end=5086
  _EVENTPAYLOADENUMMAPEVENT._serialized_start=5089
  _EVENTPAYLOADENUMMAPEVENT._serialized_end=5248
  _EVENTPAYLOADENUMMAPEVENT_ENUMMAPENTRY._serialized_start=5202
  _EVENTPAYLOADENUMMAPEVENT_ENUMMAPENTRY._serialized_end=5248
  _EVENTPAYLOADINTMAPEVENT._serialized_start=5251
  _EVENTPAYLOADINTMAPEVENT._serialized_end=5405
  _EVENTPAYLOADINTMAPEVENT_INTMAPENTRY._serialized_start=5360
  _EVENTPAYLOADINTMAPEVENT_INTMAPENTRY._serialized_end=5405
  _EVENTPAYLOADSTRMAPEVENT._serialized_start=5408
  _EVENTPAYLOADSTRMAPEVENT._serialized_end=5562
  _EVENTPAYLOADSTRMAPEVENT_STRMAPENTRY._serialized_start=5517
  _EVENTPAYLOADSTRMAPEVENT_STRMAPENTRY._serialized_end=5562
  _EVENTPAYLOADTIMESTAMPMAPEVENT._serialized_start=5565
  _EVENTPAYLOADTIMESTAMPMAPEVENT._serialized_end=5749
  _EVENTPAYLOADTIMESTAMPMAPEVENT_TIMESTAMPMAPENTRY._serialized_start=5698
  _EVENTPAYLOADTIMESTAMPMAPEVENT_TIMESTAMPMAPENTRY._serialized_end=5749
  _EVENTPAYLOADDEPRECATEDEVENT._serialized_start=5751
  _EVENTPAYLOADDEPRECATEDEVENT._serialized_end=5780
  _EVENTPAYLOADDEPRECATEDPROPERTYEVENT._serialized_start=5783
  _EVENTPAYLOADDEPRECATEDPROPERTYEVENT._serialized_end=5944
  _EVENTPAYLOADKOTLINKEYWORDEVENT._serialized_start=5947
  _EVENTPAYLOADKOTLINKEYWORDEVENT._serialized_end=6791
  _EVENTPAYLOADJAVASCRIPTKEYWORDEVENT._serialized_start=6794
  _EVENTPAYLOADJAVASCRIPTKEYWORDEVENT._serialized_end=8246
  _EVENTPAYLOADSWIFTKEYWORDEVENT._serialized_start=8249
  _EVENTPAYLOADSWIFTKEYWORDEVENT._serialized_end=10304
  _EVENTPAYLOADPYTHONKEYWORDEVENT._serialized_start=10307
  _EVENTPAYLOADPYTHONKEYWORDEVENT._serialized_end=11263
  _EVENTPAYLOADIOSONLYEVENT._serialized_start=11265
  _EVENTPAYLOADIOSONLYEVENT._serialized_end=11379
  _EVENTPAYLOAD._serialized_start=11382
  _EVENTPAYLOAD._serialized_end=13999
# @@protoc_insertion_point(module_scope)
