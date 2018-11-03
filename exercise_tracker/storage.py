from pathlib import Path
import json

from django.contrib.staticfiles.storage import ManifestFilesMixin
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(ManifestFilesMixin, S3Boto3Storage):
    def read_manifest(self):
        try:
            with open(self.manifest_name) as manifest:
                return manifest.read()
        except FileNotFoundError:
            return None

    def save_manifest(self):
        if Path(self.manifest_name).is_file():
            Path(self.manifest_name).unlink()
        with open(self.manifest_name, 'w') as manifest:
            json.dump(
                {
                    'paths': self.hashed_files,
                    'version': self.manifest_version,
                },
                manifest,
            )
