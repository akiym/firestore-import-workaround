# firestore-import-workaround

## Problem

Currently (Oct 21, 2023), firestore data exported by `gcloud` command cannot be imported to firebase emulator due to the following error:

```
Oct 21, 2023 8:49:22 PM com.google.cloud.datastore.emulator.firestore.CloudFirestore main
SEVERE: Exiting due to unexpected exception.
com.google.cloud.datastore.core.exception.DatastoreException: Message missing required fields: kind_info[0].kind
at com.google.cloud.datastore.util.leveldb.ExportImportUtil.parseBackupFile(ExportImportUtil.java:378)
at com.google.cloud.datastore.util.leveldb.ExportImportUtil.fetchEntities(ExportImportUtil.java:88)
at com.google.cloud.datastore.emulator.firestore.CloudFirestore.init(CloudFirestore.java:181)
at com.google.cloud.datastore.emulator.firestore.CloudFirestore.startLocally(CloudFirestore.java:115)
at com.google.cloud.datastore.emulator.firestore.CloudFirestore.main(CloudFirestore.java:96)
Caused by: com.google.protobuf.InvalidProtocolBufferException: Message missing required fields: kind_info[0].kind
at com.google.protobuf.UninitializedMessageException.asInvalidProtocolBufferException(UninitializedMessageException.java:79)
at com.google.protobuf.AbstractParser.checkMessageInitialized(AbstractParser.java:73)
at com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:91)
at com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:96)
at com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:48)
at com.google.cloud.datastore.util.leveldb.ExportImportUtil.parseBackupFile(ExportImportUtil.java:376)
... 4 more
```

The cause is in the exported data. The exported data has the following structure:

```
2023-10-21T10:49:07_61766
├── 2023-10-21T10:49:07_61766.overall_export_metadata
└── all_namespaces
    └── all_kinds
        ├── all_namespaces_all_kinds.export_metadata
        └── output-0
```

From the error message, I guess that this problem is in `all_namespaces_all_kinds.export_metadata` file. This file is a binary file, but contents inside are protocol buffer and dumped it into encoded text format.

```
backup_info {
  backup_name: "2023-10-21T10:49:07_61766"
  start_timestamp: 1697885347297211
}
kind_info {
  file: "output-0"
}
```

Prior to this problem, the format was as follows like. Missing are `backup_info.start_timestamp`, `kind_info.kind` and `kind_info.entity_schema.kind`. Firebase emulator requires these fields.

```
backup_info {
  backup_name: "2023-10-21T10:49:07_61766"
  start_timestamp: 1697885347297211
  end_timestamp: ...
}
kind_info {
  kind: "__all__"
  file: "output-0"
  entity_schema {
    kind: "__all__"
  }
}
```

## How to use workaround

1. Export firestore data from your GCP project

```
gcloud firestore export gs://<bucket_name>
```

2. Download exported data

```
gsutil -m cp -r "gs://<bucket_name>/<export_dir>" .
```

3. Fix exported data with `workaround.py`

```
poetry install
poetry run python workaround.py <export_dir>
```

This modifies `all_namespaces_all_kinds.export_metadata` in the exported data. Please make sure that your exported data is backed up before running this script.

## By the way, where is protobuf definition?

This come from firestore emulator's jar file. But this was defined as protobuf's descriptor data, so I dumped it (using my tool) into .proto format for easy handling.

## Tested versions

```
% firebase --version
12.7.0
% gcloud version
Google Cloud SDK 451.0.1
bq 2.0.98
core 2023.10.18
gcloud-crc32c 1.0.0
gsutil 5.26
```