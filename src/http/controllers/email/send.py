import boto3
from botocore.exceptions import ClientError


def send(template, args):
    try:
        ses_client = boto3.client('ses')

        params = {
            'Destination': {
                'ToAddresses': [args['to']],
            },
            'Message': {
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': template,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': args['subject'],
                },
            },
            'Source': 'Teste mail. <noreply@teste.com.br>',
        }
        ses_client.send_email(**params)
    except ClientError as e:
        raise e
