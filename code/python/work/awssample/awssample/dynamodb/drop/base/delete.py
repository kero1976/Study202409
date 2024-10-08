"""
DynamoDB テーブル削除用ファイル
"""
from logging import getLogger

from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


def delete_table(client, table_name: str) -> None:
    """テーブル削除

    Args:
        client (_type_): _description_
        table_name (str): テーブル名
    """
    logger.debug({"startus": "start", "params": {"client": client, "table_name": table_name}})
    try:
        # テーブルの削除を実行
        client.delete_table(TableName=table_name)

        # 削除が完了するまで待機
        waiter = client.get_waiter("table_not_exists")
        waiter.wait(TableName=table_name)

        logger.info({"status": "success", "message": f"Table {table_name} deleted successfully."})
    except ClientError as e:
        # テーブルが存在しない場合は例外を無視
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.info({"status": "success", "message": f"Table {table_name} does not exist."})
        else:
            raise
