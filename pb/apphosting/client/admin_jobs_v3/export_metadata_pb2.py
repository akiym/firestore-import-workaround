# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apphosting/client/admin_jobs_v3/export_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from apphosting.client.admin_jobs_v3 import entity_set_spec_pb2 as apphosting_dot_client_dot_admin__jobs__v3_dot_entity__set__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5apphosting/client/admin_jobs_v3/export_metadata.proto\x12\x1f\x61pphosting.client.admin_jobs_v3\x1a\x35\x61pphosting/client/admin_jobs_v3/entity_set_spec.proto\"n\n\x15OverallExportMetadata\x12U\n\x0f\x65xport_pointers\x18\x01 \x03(\x0b\x32<.apphosting.client.admin_jobs_v3.SingleExportMetadataPointer\"\xad\x01\n\x1bSingleExportMetadataPointer\x12G\n\x0f\x65ntity_set_spec\x18\x01 \x01(\x0b\x32..apphosting.client.admin_jobs_v3.EntitySetSpec\x12\x1c\n\x14\x65xport_metadata_file\x18\x02 \x01(\t\x12\x14\n\x0cnum_entities\x18\x03 \x01(\x03\x12\x11\n\tnum_bytes\x18\x04 \x01(\x03\x42\x41\n(com.google.apphosting.client.adminjobsv3B\x13\x45xportMetadataProtoP\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apphosting.client.admin_jobs_v3.export_metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.apphosting.client.adminjobsv3B\023ExportMetadataProtoP\001'
  _globals['_OVERALLEXPORTMETADATA']._serialized_start=145
  _globals['_OVERALLEXPORTMETADATA']._serialized_end=255
  _globals['_SINGLEEXPORTMETADATAPOINTER']._serialized_start=258
  _globals['_SINGLEEXPORTMETADATAPOINTER']._serialized_end=431
# @@protoc_insertion_point(module_scope)
