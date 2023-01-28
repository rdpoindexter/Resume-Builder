import boto3

db = boto3.resource('dynamodb')
#client = boto3.client('dynamodb')

def lambda_handler(event, context):
    table = db.Table('VisitorCount')

    response = table.update_item(
        Key={'Visitor': 2 },
        UpdateExpression= 'ADD V :inc',
        ExpressionAttributeValues={':inc':1}
        )

def lambda_handler(event, context):
    table = db.Table('VisitorCount')
    
    response = table.get_item(
        Key={'Visitor': 2 },
    ProjectionExpression = 'V'
        )
        
    return response



