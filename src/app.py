import json
import os
from typing import Any, Dict

from src.http.controllers.email.send import send
from src.utils.getTemplateFromS3 import get_template_from_s3
from src.utils.template.templateParser import template_parser


class App:
    def __init__(self, event: dict, context: Any):
        self.event = event
        self.context = context
        self.S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "")
        self.EMAIL_TEMPLATE_PATH = "email-templates"

    def run(self):
        try:
            for record in self.event.get("Records", []):
                data = json.loads(record.get("body", "{}"))
                template_name = data.get("template", "")
                args = data.get("args", {})
                template_file = get_template_from_s3(self.S3_BUCKET_NAME, f"{self.EMAIL_TEMPLATE_PATH}/{template_name}")
                parser = template_parser(template_file, args)
                send(template=parser, args=args)
        except Exception as e:
            print(f"Error: {e}")
            raise e
