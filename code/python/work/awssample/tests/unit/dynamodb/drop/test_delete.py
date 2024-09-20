from awssample.connect.connect import Connect
from awssample.dynamodb.drop.delete import Delete
from moto import mock_aws


def test_delete():
    conn = Connect("dynamodb")
    dynamo = Delete(conn)
    dynamo.delete_table("foo2")
    assert True
