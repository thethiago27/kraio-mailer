import boto3
from botocore.exceptions import ClientError


def get_template_from_s3(bucket: str, key: str) -> str:
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket, Key=key)
        return response['Body'].read().decode('utf-8')
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise FileNotFoundError(f"File {key} not found in bucket {bucket}")
        else:
            raise
