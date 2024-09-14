import boto3
from awssample.dynamodb.create.create import create_table

resource = boto3.resource("dynamodb")

create_table(resource, "foo1")
