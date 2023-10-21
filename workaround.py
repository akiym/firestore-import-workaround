import sys
from pathlib import Path

from pb.apphosting.ext.datastore_admin.backup_pb2 import Backup

if len(sys.argv) != 2:
    print('Usage: workaround.py <export_dir>')
    sys.exit(1)

export_dir = Path(sys.argv[1])

export_metadata_file = export_dir / 'all_namespaces/all_kinds/all_namespaces_all_kinds.export_metadata'
export_metadata = Backup.FromString(export_metadata_file.read_bytes())

kind_info = export_metadata.kind_info[0]
assert kind_info
kind_info.kind = '__all__'
kind_info.entity_schema.kind = '__all__'

with export_metadata_file.open('wb') as f:
    f.write(export_metadata.SerializeToString())