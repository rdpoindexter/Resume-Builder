import boto3
import json
import requests

db = boto3.resource('dynamodb')

def lambda_handler(event, context):


def counter_increment():
    table = db.Table('VisitorCount')
    response = table.update_item(
        Key={'Visitor': 2 },
        UpdateExpression= 'ADD Vcount :inc',
        ExpressionAttributeValues={':inc':1}
        )