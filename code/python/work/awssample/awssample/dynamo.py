import boto3
from awssample.dynamodb.create.base.create import create_table

print("START")
# DynamoDBのクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')



# テーブルを作成する関数を実行
create_table(dynamodb, "hoge2")