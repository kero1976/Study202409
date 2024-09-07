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

def create_table(resource, table_name: str):
    logger.debug({
        "startus": "start",
        "params": {
            "resource": resource,
            "table_name": table_name
        }
    })
    try:
        # テーブルの作成
        table = resource.create_table(
            TableName=table_name,  # テーブル名
            KeySchema=[
                {
                    'AttributeName': 'id',  # パーティションキーの属性名
                    'KeyType': 'HASH'  # パーティションキー
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # 文字列型 (S: String, N: Number, B: Binary)
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,  # 読み取りキャパシティ
                'WriteCapacityUnits': 5  # 書き込みキャパシティ
            }
        )

        # テーブルが作成されるまで待機
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print("テーブルが正常に作成されました")
        logger.info({
            "startus": "success",
            "result": table
        })
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        logger.error({
            "startus": "fail",
            "exception": e
        })