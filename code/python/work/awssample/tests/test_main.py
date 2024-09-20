from awssample.connect.connect import Connect
from awssample.dynamodb.create.create import Create
from awssample.dynamodb.drop.delete import Delete


def test_case1():
    """テーブルを作成し、テーブルを削除する
    """
    dynamodb = Connect("dynamodb")
    Create(dynamodb).create_table("foo")
    Delete(dynamodb).delete_table("foo")
