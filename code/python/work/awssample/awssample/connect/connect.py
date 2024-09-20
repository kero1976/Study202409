"""
AWS Connnector.

create boto3.resource and boto3.client
"""
from logging import getLogger

import boto3

# ロガーの作成
logger = getLogger(__name__)


class Connect():
    """AWS Connnector.

    create boto3.resource and boto3.client
    """

    def __init__(self, service: str):
        """コンストラクタ

        Args:
            service (str): サービス名
        """
        self.service = service

    def get_resource(self):
        """resourceの取得

        Returns:
            _type_: resource
        """
        return boto3.resource(self.service)

    def get_client(self):
        """clientの取得

        Returns:
            _type_: client
        """
        return boto3.client(self.service)
