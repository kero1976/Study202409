import logging

import boto3
from awssample.dynamodb.insert.base.insert import add_item

# logging.getLogger("botocore").setLevel(logging.ERROR)
# logging.getLogger("urllib3").setLevel(logging.ERROR)
# logging.getLogger("boto3").setLevel(logging.ERROR)


def test_add_item():

    resource = boto3.resource("dynamodb")

    result = add_item(resource, "foo1", {"id": "A6", "data": "BBB5"})
    assert result
