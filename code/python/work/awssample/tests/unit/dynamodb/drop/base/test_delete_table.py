import logging
from unittest.mock import MagicMock, patch

import boto3
import pytest
from awssample.dynamodb.drop.base.delete import delete_table
from botocore.exceptions import ClientError

# logging.getLogger("botocore").setLevel(logging.ERROR)
# logging.getLogger("urllib3").setLevel(logging.ERROR)
# logging.getLogger("boto3").setLevel(logging.ERROR)


def test_delete_table():

    resource = boto3.client("dynamodb")

    delete_table(resource, "sample_table4")
    assert True


def test_delete_table_raises_unexpected_error():
    resource_mock = MagicMock()
    resource_mock.delete_table.side_effect = ClientError(
        {"Error": {
            "Code": "500",
            "Message": "Internal Server Error"
        }}, "ListTables")
    with pytest.raises(ClientError):
        delete_table(resource_mock, "A")
