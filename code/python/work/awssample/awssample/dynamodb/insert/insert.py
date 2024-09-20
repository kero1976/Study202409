"""
DynamoDB データの登録
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.insert.base.insert import add_item
from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


# DynamoDBのテーブルにデータを追加する関数
def add_item2(connect: Connect, table_name: str, item: dict):
    """
    DynamoDBテーブルにデータを追加する関数

    :param table_name: テーブル名
    :param item: 追加するデータ（辞書形式）
    :return: 成功した場合はTrue、失敗した場合はFalse
    """
    logger.debug({
        "status": "start",
        "params": {
            "connect": connect,
            "table_name": table_name,
            "item": item
        }
    })
    add_item(connect.get_client(), table_name, item)
