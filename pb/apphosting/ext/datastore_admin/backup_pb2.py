# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apphosting/ext/datastore_admin/backup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+apphosting/ext/datastore_admin/backup.proto\x12\x1e\x61pphosting.ext.datastore_admin\"\x8c\x01\n\x06\x42\x61\x63kup\x12?\n\x0b\x62\x61\x63kup_info\x18\x01 \x01(\x0b\x32*.apphosting.ext.datastore_admin.BackupInfo\x12\x41\n\tkind_info\x18\x02 \x03(\x0b\x32..apphosting.ext.datastore_admin.KindBackupInfo\"Q\n\nBackupInfo\x12\x13\n\x0b\x62\x61\x63kup_name\x18\x01 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x02 \x01(\x03\x12\x15\n\rend_timestamp\x18\x03 \x01(\x03\"\x8c\x01\n\x0eKindBackupInfo\x12\x0c\n\x04kind\x18\x01 \x02(\t\x12\x0c\n\x04\x66ile\x18\x02 \x03(\t\x12\x43\n\rentity_schema\x18\x03 \x01(\x0b\x32,.apphosting.ext.datastore_admin.EntitySchema\x12\x19\n\nis_partial\x18\x04 \x01(\x08:\x05\x66\x61lse\"\x90\x05\n\x0c\x45ntitySchema\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x41\n\x05\x66ield\x18\x02 \x03(\x0b\x32\x32.apphosting.ext.datastore_admin.EntitySchema.Field\x1a\xb2\x01\n\x04Type\x12\x0f\n\x07is_list\x18\x01 \x01(\x08\x12R\n\x0eprimitive_type\x18\x02 \x03(\x0e\x32:.apphosting.ext.datastore_admin.EntitySchema.PrimitiveType\x12\x45\n\x0f\x65mbedded_schema\x18\x03 \x03(\x0b\x32,.apphosting.ext.datastore_admin.EntitySchema\x1aj\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x02(\t\x12?\n\x04type\x18\x02 \x03(\x0b\x32\x31.apphosting.ext.datastore_admin.EntitySchema.Type\x12\x12\n\nfield_name\x18\x03 \x01(\t\"\x8d\x02\n\rPrimitiveType\x12\t\n\x05\x46LOAT\x10\x00\x12\x0b\n\x07INTEGER\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\n\n\x06STRING\x10\x03\x12\r\n\tDATE_TIME\x10\x04\x12\n\n\x06RATING\x10\x05\x12\x08\n\x04LINK\x10\x06\x12\x0c\n\x08\x43\x41TEGORY\x10\x07\x12\x10\n\x0cPHONE_NUMBER\x10\x08\x12\x12\n\x0ePOSTAL_ADDRESS\x10\t\x12\t\n\x05\x45MAIL\x10\n\x12\r\n\tIM_HANDLE\x10\x0b\x12\x0c\n\x08\x42LOB_KEY\x10\x0c\x12\x08\n\x04TEXT\x10\r\x12\x08\n\x04\x42LOB\x10\x0e\x12\x0e\n\nSHORT_BLOB\x10\x0f\x12\x08\n\x04USER\x10\x10\x12\r\n\tGEO_POINT\x10\x11\x12\r\n\tREFERENCE\x10\x12\x42\x0e\x42\x0c\x42\x61\x63kupProtos')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apphosting.ext.datastore_admin.backup_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'B\014BackupProtos'
  _globals['_BACKUP']._serialized_start=80
  _globals['_BACKUP']._serialized_end=220
  _globals['_BACKUPINFO']._serialized_start=222
  _globals['_BACKUPINFO']._serialized_end=303
  _globals['_KINDBACKUPINFO']._serialized_start=306
  _globals['_KINDBACKUPINFO']._serialized_end=446
  _globals['_ENTITYSCHEMA']._serialized_start=449
  _globals['_ENTITYSCHEMA']._serialized_end=1105
  _globals['_ENTITYSCHEMA_TYPE']._serialized_start=547
  _globals['_ENTITYSCHEMA_TYPE']._serialized_end=725
  _globals['_ENTITYSCHEMA_FIELD']._serialized_start=727
  _globals['_ENTITYSCHEMA_FIELD']._serialized_end=833
  _globals['_ENTITYSCHEMA_PRIMITIVETYPE']._serialized_start=836
  _globals['_ENTITYSCHEMA_PRIMITIVETYPE']._serialized_end=1105
# @@protoc_insertion_point(module_scope)
