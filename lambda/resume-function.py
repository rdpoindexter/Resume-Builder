import boto3

db = boto3.resource('dynamodb')
#client = boto3.client('dynamodb')

def lambda_handler(event, context):
    table = db.Table('VisitorCount')

    response = table.put_item(
        Item={'Visitor': '3'})


def lambda_handler(event, context):
    table = db.Table('VisitorCount')

    response = table.update_item(
        Key={'Visitor': 2 },
        UpdateExpression= 'ADD Vcount :inc',
        ExpressionAttributeValues={':inc':1}
        )



