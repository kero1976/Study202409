import logging

import boto3
from awssample.dynamodb.drop.base.delete import delete_table

# logging.getLogger("botocore").setLevel(logging.ERROR)
# logging.getLogger("urllib3").setLevel(logging.ERROR)
# logging.getLogger("boto3").setLevel(logging.ERROR)


def test_delete_table():

    resource = boto3.client("dynamodb")

    delete_table(resource, "sample_table4")
    assert True
