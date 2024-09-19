from logging import getLogger

import boto3
from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


class Connect():

    def __init__(self, service):
        self.service = service

    def get_resource(self):
        return boto3.resource(self.service)

    def get_client(self):
        return boto3.client(self.service)
