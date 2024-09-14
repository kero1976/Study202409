import logging

import boto3
from awssample.dynamodb.create.base.create import (create_table, create_table_if_not_exists)

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)


def test_create_table():

    resource = boto3.resource("dynamodb")
    keySchema = [{
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
    table = create_table_if_not_exists(resource, "sample_table5", keySchema, attribute_definitions,
                                       provisioned_throughput)
    assert table
