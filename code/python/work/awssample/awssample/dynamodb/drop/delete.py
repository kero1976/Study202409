"""
DynamoDB テーブル削除用ファイル
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.drop.base.delete import delete_table
from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


def delete_table2(connect: Connect, table_name: str) -> None:
    """テーブル削除

    Args:
        connect (Connect): _description_
        table_name (str): テーブル名
    """
    logger.debug({"startus": "start", "params": {"connect": connect, "table_name": table_name}})
    delete_table(connect.get_client(), table_name)
    logger.debug({"startus": "success"})
