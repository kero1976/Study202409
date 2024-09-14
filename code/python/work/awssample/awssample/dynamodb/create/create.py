"""
DynamoDBのテーブル作成用ファイル
"""
from logging import getLogger

from awssample.dynamodb.create.base.create import create_table_if_not_exists

# ロガーの作成
logger = getLogger(__name__)


def create_table(resource, table_name: str) -> None:
    """テーブル作成(冪等)

    Args:
        resource (_type_): _description_
        table_name (str): _description_
    """
    logger.debug({"startus": "start", "params": {"resource": resource, "table_name": table_name}})
    key_schema = [{
        "AttributeName": "id",  # パーティションキーの属性名
        "KeyType": "HASH"  # パーティションキー
    }]

    attribute_definitions = [{
        "AttributeName": "id",
        "AttributeType": "S"  # 文字列型 (S: String, N: Number, B: Binary)
    }]

    provisioned_throughput = {
        "ReadCapacityUnits": 5,  # 読み取りキャパシティ
        "WriteCapacityUnits": 5  # 書き込みキャパシティ
    }
    create_table_if_not_exists(resource, table_name, key_schema, attribute_definitions,
                               provisioned_throughput)

    logger.info({"status": "success"})
