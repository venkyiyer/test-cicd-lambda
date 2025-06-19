import json

def lambda_handler(event, context):
    #TO DO STUFF
    return {
        'statusCode':200, 
        'body':json.dumps('Hello from Lambda')
    }
