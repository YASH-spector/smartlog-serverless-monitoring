import json
import boto3
import uuid
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = "paste_your_table_name"
SNS_TOPIC_ARN = "PASTE_YOUR_SNS_TOPIC_ARN"
BUCKET_NAME = "paste_your_bucket_name"

def lambda_handler(event, context):

    body = json.loads(event['body'])

    log_level = body.get("level")
    message = body.get("message")
    service = body.get("service")

    log_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    log_data = {
        "logId": log_id,
        "timestamp": timestamp,
        "logLevel": log_level,
        "message": message,
        "service": service
    }

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=log_data)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"logs/{log_id}.json",
        Body=json.dumps(log_data)
    )

    if log_level == "ERROR":
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="SmartLog Error Alert",
            Message=f"Error detected in {service}: {message}"
        )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Log processed"})
    }
