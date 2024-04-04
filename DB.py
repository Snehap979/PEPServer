import boto3
TableName='pepdatabase'
# Initialize DynamoDB client
dynamodb = boto3.client(
    'dynamodb',
    region_name='us-west-1',
    aws_access_key_id='AKIATCKAM2M6EZWVAP3Q',
    aws_secret_access_key='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'
)
from datetime import datetime, time

def checkUserExists(username,):
    try:
        # Save user information to DynamoDB
        response = dynamodb.put_item(
            TableName='pepdatabase',
            Item={
                'user_id':{'S': '1234568'},
                'email': {'S': username}
               
                
            }
        )
        return True
    except Exception as e:
        print("Error saving user info:", e)
        return False

def saveUser(username,email):
    try:
        # Save user information to DynamoDB
        response = dynamodb.put_item(
            TableName='pepdatabase',
            Item={
                'user_id':{'S': username},
                'email': {'S': email}                
            }
        )
        return True
    except Exception as e:
        print("Error saving user info:", e)
        return False
    




def saveUser(username,email):
    try:
        # Save user information to DynamoDB
        response = dynamodb.put_item(
            TableName='pepdatabase',
            Item={
                'user_id':{'S': username},
                'email': {'S': email}                
            }
        )
        return True
    except Exception as e:
        print("Error saving user info:", e)
        return False



def getItems(N,startTime,endTime):
    try:
         table_name = "energyconsumption"
         key = {
          "  deviceTypeId": {
          "N": N
         }
    }   
         get_item_params = {
    'TableName': table_name,
    'Key': key,
}
         response = dynamodb.get_item(**get_item_params)
         values_within_range = []
         startTime = datetime.strptime(startTime, "%H:%M").time()
         endTime = datetime.strptime(endTime, "%H:%M").time()
         for item in response['Item']['values']['L']:
           item_time = item["M"]["time"]["S"]
           item_time=datetime.strptime(item_time, "%H:%M").time()
           if startTime <= item_time <= endTime:       
            values_within_range.append(item['M'])
            print("values_within_range",values_within_range)
         return values_within_range

    except Exception as e:
         return False
    

  