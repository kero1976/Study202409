from logging import getLogger, StreamHandler, DEBUG, Formatter

# ロガーの作成
logger = getLogger(__name__)
logger.setLevel(DEBUG)  # ロガーのレベルをDEBUGに設定

# コンソールにログメッセージを表示するハンドラを作成
console_handler = StreamHandler()
format = Formatter("%(asctime)s:%(funcName)s:%(message)s")
console_handler.setFormatter(format)

# ハンドラをロガーに追加
logger.addHandler(console_handler)

# ログメッセージの出力
logger.debug("Debug レベルのログメッセージ")

def create_table_simple(resource, table_name: str):
    KeySchema=[
        {
            'AttributeName': 'id',  # パーティションキーの属性名
            'KeyType': 'HASH'  # パーティションキー
        }
    ]

    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  # 文字列型 (S: String, N: Number, B: Binary)
        }
    ]
    
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,  # 読み取りキャパシティ
        'WriteCapacityUnits': 5  # 書き込みキャパシティ
    }
    create_table(resource, table_name, KeySchema, AttributeDefinitions, ProvisionedThroughput)

def create_table(resource, table_name: str, key_schema: list[dict], attribute_definitions: list[dict], provisioned_throughput: dict):
    logger.debug({
        "startus": "start",
        "params": {
            "resource": resource,
            "table_name": table_name,
            "key_schema": key_schema,
            "attribute_definitions": attribute_definitions,
            "provisioned_throughput": provisioned_throughput
        }
    })
    try:
        # テーブルの作成
        table = resource.create_table(
            TableName=table_name,  # テーブル名
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput=provisioned_throughput
        )

        # テーブルが作成されるまで待機
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        logger.info({
            "startus": "success",
            "result": table
        })
    
    except Exception as e:
        logger.error({
            "startus": "fail",
            "exception": e
        })