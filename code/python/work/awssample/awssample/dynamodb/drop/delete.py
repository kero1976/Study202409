"""
DynamoDB テーブル削除用ファイル
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.drop.base import delete

# ロガーの作成
logger = getLogger(__name__)


class Delete():
    """DynamoDB テーブル削除用クラス
    """

    def __init__(self, connect: Connect):
        self.connect = connect

    def delete_table(self, table_name: str) -> None:
        """テーブル削除

        Args:
            table_name (str): テーブル名
        """
        logger.debug({"status": "start", "params": {"table_name": table_name}})
        delete.delete_table(self.connect.get_client(), table_name)
        logger.debug({"status": "success"})
