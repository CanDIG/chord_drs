import boto3
from flask import current_app
from chord_drs.backends.base import Backend


class MinioBackend(Backend):
    def __init__(self, resource=None):
        if resource:
            self.minio = resource
        else:
            self.minio = boto3.resource(
                's3',
                endpoint_url=current_app.config['MINIO_URL'],
                aws_access_key_id=current_app.config['MINIO_USERNAME'],
                aws_secret_access_key=current_app.config['MINIO_PASSWORD']
            )

        self.bucket = self.minio.Bucket(current_app.config['MINIO_BUCKET'])

    def build_minio_location(self, obj):
        return f"s3://{current_app.config['MINIO_URL']}/{obj.bucket_name}/{obj.key}"

    def get_minio_object(self, location: str):
        obj = self.bucket.Object(location.split('/')[-1])

        return obj.get()

    def save(self, current_location: str, filename: str) -> str:
        f = open(current_location, 'rb')

        obj = self.bucket.put_object(Key=filename, Body=f)

        return self.build_minio_location(obj)
