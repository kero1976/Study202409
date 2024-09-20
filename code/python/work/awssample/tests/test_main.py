from datetime import datetime

import boto3
from awssample.dynamodb.create.create import Create
from awssample.dynamodb.drop.base.delete import delete_table
from awssample.dynamodb.insert.base.insert import add_item

resource = boto3.resource("dynamodb")
client = boto3.client("dynamodb")

TABLE_NAME = "shijo_test"
# print(f"{datetime.now().strftime('%H:%M:%S')}:START")
# create_table(client, TABLE_NAME)
# print(f"{datetime.now().strftime('%H:%M:%S')}:テーブルを作成しました")
# add_item(resource, TABLE_NAME, {"id": "aaa"})
# print(f"{datetime.now().strftime('%H:%M:%S')}:データを追加しました")
# delete_table(client, TABLE_NAME)
# print(f"{datetime.now().strftime('%H:%M:%S')}:END")
