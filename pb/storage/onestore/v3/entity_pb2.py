# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage/onestore/v3/entity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n storage/onestore/v3/entity.proto\x12\x13storage_onestore_v3\"\xd1\x05\n\rPropertyValue\x12\x12\n\nint64Value\x18\x01 \x01(\x03\x12\x14\n\x0c\x62ooleanValue\x18\x02 \x01(\x08\x12\x13\n\x0bstringValue\x18\x03 \x01(\t\x12\x13\n\x0b\x64oubleValue\x18\x04 \x01(\x01\x12\x41\n\npointvalue\x18\x05 \x01(\n2-.storage_onestore_v3.PropertyValue.PointValue\x12?\n\tuservalue\x18\x08 \x01(\n2,.storage_onestore_v3.PropertyValue.UserValue\x12I\n\x0ereferencevalue\x18\x0c \x01(\n21.storage_onestore_v3.PropertyValue.ReferenceValue\x1a\"\n\nPointValue\x12\t\n\x01x\x18\x06 \x02(\x01\x12\t\n\x01y\x18\x07 \x02(\x01\x1a\xa4\x01\n\tUserValue\x12\r\n\x05\x65mail\x18\t \x02(\t\x12\x13\n\x0b\x61uth_domain\x18\n \x02(\t\x12\x10\n\x08nickname\x18\x0b \x01(\t\x12\x0e\n\x06gaiaid\x18\x12 \x02(\x03\x12\x19\n\x11obfuscated_gaiaid\x18\x13 \x01(\t\x12\x1a\n\x12\x66\x65\x64\x65rated_identity\x18\x15 \x01(\t\x12\x1a\n\x12\x66\x65\x64\x65rated_provider\x18\x16 \x01(\t\x1a\xd1\x01\n\x0eReferenceValue\x12\x0b\n\x03\x61pp\x18\r \x02(\t\x12\x12\n\nname_space\x18\x14 \x01(\t\x12R\n\x0bpathelement\x18\x0e \x03(\n2=.storage_onestore_v3.PropertyValue.ReferenceValue.PathElement\x12\x13\n\x0b\x64\x61tabase_id\x18\x17 \x01(\t\x1a\x35\n\x0bPathElement\x12\x0c\n\x04type\x18\x0f \x02(\t\x12\n\n\x02id\x18\x10 \x01(\x03\x12\x0c\n\x04name\x18\x11 \x01(\t\"\xbc\x04\n\x08Property\x12\x42\n\x07meaning\x18\x01 \x01(\x0e\x32%.storage_onestore_v3.Property.Meaning:\nNO_MEANING\x12\x13\n\x0bmeaning_uri\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x31\n\x05value\x18\x05 \x02(\x0b\x32\".storage_onestore_v3.PropertyValue\x12\x10\n\x08multiple\x18\x04 \x02(\x08\x12\x13\n\x07stashed\x18\x06 \x01(\x05:\x02-1\x12\x17\n\x08\x63omputed\x18\x07 \x01(\x08:\x05\x66\x61lse\"\xd5\x02\n\x07Meaning\x12\x0e\n\nNO_MEANING\x10\x00\x12\x08\n\x04\x42LOB\x10\x0e\x12\x08\n\x04TEXT\x10\x0f\x12\x0e\n\nBYTESTRING\x10\x10\x12\x11\n\rATOM_CATEGORY\x10\x01\x12\r\n\tATOM_LINK\x10\x02\x12\x0e\n\nATOM_TITLE\x10\x03\x12\x10\n\x0c\x41TOM_CONTENT\x10\x04\x12\x10\n\x0c\x41TOM_SUMMARY\x10\x05\x12\x0f\n\x0b\x41TOM_AUTHOR\x10\x06\x12\x0b\n\x07GD_WHEN\x10\x07\x12\x0c\n\x08GD_EMAIL\x10\x08\x12\x10\n\x0cGEORSS_POINT\x10\t\x12\t\n\x05GD_IM\x10\n\x12\x12\n\x0eGD_PHONENUMBER\x10\x0b\x12\x14\n\x10GD_POSTALADDRESS\x10\x0c\x12\r\n\tGD_RATING\x10\r\x12\x0b\n\x07\x42LOBKEY\x10\x11\x12\x10\n\x0c\x45NTITY_PROTO\x10\x13\x12\x0e\n\nEMPTY_LIST\x10\x18\x12\x0f\n\x0bINDEX_VALUE\x10\x12\"m\n\x04Path\x12\x32\n\x07\x65lement\x18\x01 \x03(\n2!.storage_onestore_v3.Path.Element\x1a\x31\n\x07\x45lement\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\n\n\x02id\x18\x03 \x01(\x03\x12\x0c\n\x04name\x18\x04 \x01(\t\"j\n\tReference\x12\x0b\n\x03\x61pp\x18\r \x02(\t\x12\x12\n\nname_space\x18\x14 \x01(\t\x12\'\n\x04path\x18\x0e \x02(\x0b\x32\x19.storage_onestore_v3.Path\x12\x13\n\x0b\x64\x61tabase_id\x18\x17 \x01(\t\"\x9f\x01\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x02(\t\x12\x13\n\x0b\x61uth_domain\x18\x02 \x02(\t\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x0e\n\x06gaiaid\x18\x04 \x02(\x03\x12\x19\n\x11obfuscated_gaiaid\x18\x05 \x01(\t\x12\x1a\n\x12\x66\x65\x64\x65rated_identity\x18\x06 \x01(\t\x12\x1a\n\x12\x66\x65\x64\x65rated_provider\x18\x07 \x01(\t\"\xf8\x02\n\x0b\x45ntityProto\x12+\n\x03key\x18\r \x02(\x0b\x32\x1e.storage_onestore_v3.Reference\x12/\n\x0c\x65ntity_group\x18\x10 \x02(\x0b\x32\x19.storage_onestore_v3.Path\x12(\n\x05owner\x18\x11 \x01(\x0b\x32\x19.storage_onestore_v3.User\x12\x33\n\x04kind\x18\x04 \x01(\x0e\x32%.storage_onestore_v3.EntityProto.Kind\x12\x10\n\x08kind_uri\x18\x05 \x01(\t\x12/\n\x08property\x18\x0e \x03(\x0b\x32\x1d.storage_onestore_v3.Property\x12\x33\n\x0craw_property\x18\x0f \x03(\x0b\x32\x1d.storage_onestore_v3.Property\"4\n\x04Kind\x12\x0e\n\nGD_CONTACT\x10\x01\x12\x0c\n\x08GD_EVENT\x10\x02\x12\x0e\n\nGD_MESSAGE\x10\x03\"B\n\x0e\x45ntityMetadata\x12\x17\n\x0f\x63reated_version\x18\x01 \x01(\x03\x12\x17\n\x0fupdated_version\x18\x02 \x01(\x03\"\xb5\x01\n\rEntitySummary\x12N\n\x12large_raw_property\x18\x01 \x03(\x0b\x32\x32.storage_onestore_v3.EntitySummary.PropertySummary\x1aT\n\x0fPropertySummary\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1f\n\x17property_type_for_stats\x18\x02 \x01(\t\x12\x12\n\nsize_bytes\x18\x03 \x01(\x05\"4\n\x11\x43ompositeProperty\x12\x10\n\x08index_id\x18\x01 \x02(\x03\x12\r\n\x05value\x18\x02 \x03(\t\"\xc2\x04\n\x05Index\x12\x13\n\x0b\x65ntity_type\x18\x01 \x02(\t\x12\x10\n\x08\x61ncestor\x18\x05 \x02(\x08\x12\x0e\n\x06parent\x18\x07 \x01(\x08\x12H\n\x07version\x18\x08 \x01(\x0e\x32\".storage_onestore_v3.Index.Version:\x13VERSION_UNSPECIFIED\x12\x35\n\x08property\x18\x02 \x03(\n2#.storage_onestore_v3.Index.Property\x1a\xc4\x02\n\x08Property\x12\x0c\n\x04name\x18\x03 \x02(\t\x12W\n\tdirection\x18\x04 \x01(\x0e\x32-.storage_onestore_v3.Index.Property.Direction:\x15\x44IRECTION_UNSPECIFIED\x12H\n\x04mode\x18\x06 \x01(\x0e\x32(.storage_onestore_v3.Index.Property.Mode:\x10MODE_UNSPECIFIED\"E\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\"@\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0e\n\nGEOSPATIAL\x10\x03\x12\x12\n\x0e\x41RRAY_CONTAINS\x10\x04\":\n\x07Version\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02\x12\x06\n\x02V3\x10\x03\"\xae\x04\n\x0e\x43ompositeIndex\x12\x0e\n\x06\x61pp_id\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x61tabase_id\x18\x0c \x01(\t\x12\n\n\x02id\x18\x02 \x02(\x03\x12.\n\ndefinition\x18\x03 \x02(\x0b\x32\x1a.storage_onestore_v3.Index\x12\x38\n\x05state\x18\x04 \x02(\x0e\x32).storage_onestore_v3.CompositeIndex.State\x12M\n\x0eworkflow_state\x18\n \x01(\x0e\x32\x31.storage_onestore_v3.CompositeIndex.WorkflowStateB\x02\x18\x01\x12\x19\n\rerror_message\x18\x0b \x01(\tB\x02\x18\x01\x12\'\n\x14only_use_if_required\x18\x06 \x01(\x08:\x05\x66\x61lseB\x02\x18\x01\x12!\n\x0e\x64isabled_index\x18\t \x01(\x08:\x05\x66\x61lseB\x02\x18\x01\x12\'\n\x1f\x64\x65precated_read_division_family\x18\x07 \x03(\t\x12(\n deprecated_write_division_family\x18\x08 \x01(\t\"?\n\x05State\x12\x0e\n\nWRITE_ONLY\x10\x01\x12\x0e\n\nREAD_WRITE\x10\x02\x12\x0b\n\x07\x44\x45LETED\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"7\n\rWorkflowState\x12\x0b\n\x07PENDING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\r\n\tCOMPLETED\x10\x03\"w\n\x10SearchIndexEntry\x12\x10\n\x08index_id\x18\x01 \x02(\x03\x12\x1d\n\x15write_division_family\x18\x02 \x02(\t\x12\x18\n\x10\x66ingerprint_1999\x18\x03 \x01(\x06\x12\x18\n\x10\x66ingerprint_2011\x18\x04 \x01(\x06\"\x86\x02\n\x0cIndexPostfix\x12\x41\n\x0bindex_value\x18\x01 \x03(\x0b\x32,.storage_onestore_v3.IndexPostfix.IndexValue\x12+\n\x03key\x18\x02 \x01(\x0b\x32\x1e.storage_onestore_v3.Reference\x12\x14\n\x06\x62\x65\x66ore\x18\x03 \x01(\x08:\x04true\x12\x18\n\x10\x62\x65\x66ore_ascending\x18\x04 \x01(\x08\x1aV\n\nIndexValue\x12\x15\n\rproperty_name\x18\x01 \x02(\t\x12\x31\n\x05value\x18\x02 \x02(\x0b\x32\".storage_onestore_v3.PropertyValue\"L\n\rIndexPosition\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\x06\x62\x65\x66ore\x18\x02 \x01(\x08:\x04true\x12\x18\n\x10\x62\x65\x66ore_ascending\x18\x03 \x01(\x08\x42\x45\n\x1e\x63om.google.storage.onestore.v3B\x0eOnestoreEntityZ\x13storage_onestore_v3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage.onestore.v3.entity_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.google.storage.onestore.v3B\016OnestoreEntityZ\023storage_onestore_v3'
  _globals['_COMPOSITEINDEX'].fields_by_name['workflow_state']._options = None
  _globals['_COMPOSITEINDEX'].fields_by_name['workflow_state']._serialized_options = b'\030\001'
  _globals['_COMPOSITEINDEX'].fields_by_name['error_message']._options = None
  _globals['_COMPOSITEINDEX'].fields_by_name['error_message']._serialized_options = b'\030\001'
  _globals['_COMPOSITEINDEX'].fields_by_name['only_use_if_required']._options = None
  _globals['_COMPOSITEINDEX'].fields_by_name['only_use_if_required']._serialized_options = b'\030\001'
  _globals['_COMPOSITEINDEX'].fields_by_name['disabled_index']._options = None
  _globals['_COMPOSITEINDEX'].fields_by_name['disabled_index']._serialized_options = b'\030\001'
  _globals['_PROPERTYVALUE']._serialized_start=58
  _globals['_PROPERTYVALUE']._serialized_end=779
  _globals['_PROPERTYVALUE_POINTVALUE']._serialized_start=366
  _globals['_PROPERTYVALUE_POINTVALUE']._serialized_end=400
  _globals['_PROPERTYVALUE_USERVALUE']._serialized_start=403
  _globals['_PROPERTYVALUE_USERVALUE']._serialized_end=567
  _globals['_PROPERTYVALUE_REFERENCEVALUE']._serialized_start=570
  _globals['_PROPERTYVALUE_REFERENCEVALUE']._serialized_end=779
  _globals['_PROPERTYVALUE_REFERENCEVALUE_PATHELEMENT']._serialized_start=726
  _globals['_PROPERTYVALUE_REFERENCEVALUE_PATHELEMENT']._serialized_end=779
  _globals['_PROPERTY']._serialized_start=782
  _globals['_PROPERTY']._serialized_end=1354
  _globals['_PROPERTY_MEANING']._serialized_start=1013
  _globals['_PROPERTY_MEANING']._serialized_end=1354
  _globals['_PATH']._serialized_start=1356
  _globals['_PATH']._serialized_end=1465
  _globals['_PATH_ELEMENT']._serialized_start=1416
  _globals['_PATH_ELEMENT']._serialized_end=1465
  _globals['_REFERENCE']._serialized_start=1467
  _globals['_REFERENCE']._serialized_end=1573
  _globals['_USER']._serialized_start=1576
  _globals['_USER']._serialized_end=1735
  _globals['_ENTITYPROTO']._serialized_start=1738
  _globals['_ENTITYPROTO']._serialized_end=2114
  _globals['_ENTITYPROTO_KIND']._serialized_start=2062
  _globals['_ENTITYPROTO_KIND']._serialized_end=2114
  _globals['_ENTITYMETADATA']._serialized_start=2116
  _globals['_ENTITYMETADATA']._serialized_end=2182
  _globals['_ENTITYSUMMARY']._serialized_start=2185
  _globals['_ENTITYSUMMARY']._serialized_end=2366
  _globals['_ENTITYSUMMARY_PROPERTYSUMMARY']._serialized_start=2282
  _globals['_ENTITYSUMMARY_PROPERTYSUMMARY']._serialized_end=2366
  _globals['_COMPOSITEPROPERTY']._serialized_start=2368
  _globals['_COMPOSITEPROPERTY']._serialized_end=2420
  _globals['_INDEX']._serialized_start=2423
  _globals['_INDEX']._serialized_end=3001
  _globals['_INDEX_PROPERTY']._serialized_start=2617
  _globals['_INDEX_PROPERTY']._serialized_end=2941
  _globals['_INDEX_PROPERTY_DIRECTION']._serialized_start=2806
  _globals['_INDEX_PROPERTY_DIRECTION']._serialized_end=2875
  _globals['_INDEX_PROPERTY_MODE']._serialized_start=2877
  _globals['_INDEX_PROPERTY_MODE']._serialized_end=2941
  _globals['_INDEX_VERSION']._serialized_start=2943
  _globals['_INDEX_VERSION']._serialized_end=3001
  _globals['_COMPOSITEINDEX']._serialized_start=3004
  _globals['_COMPOSITEINDEX']._serialized_end=3562
  _globals['_COMPOSITEINDEX_STATE']._serialized_start=3442
  _globals['_COMPOSITEINDEX_STATE']._serialized_end=3505
  _globals['_COMPOSITEINDEX_WORKFLOWSTATE']._serialized_start=3507
  _globals['_COMPOSITEINDEX_WORKFLOWSTATE']._serialized_end=3562
  _globals['_SEARCHINDEXENTRY']._serialized_start=3564
  _globals['_SEARCHINDEXENTRY']._serialized_end=3683
  _globals['_INDEXPOSTFIX']._serialized_start=3686
  _globals['_INDEXPOSTFIX']._serialized_end=3948
  _globals['_INDEXPOSTFIX_INDEXVALUE']._serialized_start=3862
  _globals['_INDEXPOSTFIX_INDEXVALUE']._serialized_end=3948
  _globals['_INDEXPOSITION']._serialized_start=3950
  _globals['_INDEXPOSITION']._serialized_end=4026
# @@protoc_insertion_point(module_scope)
