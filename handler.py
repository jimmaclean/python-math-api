import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def square(event, context):
    x = int(event["queryStringParameters"]['int'])
    
    response = {
        "statusCode": 200,
        "body": x * x
    }

    return response