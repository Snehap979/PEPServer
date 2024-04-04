import boto3;
client = boto3.client('cognito-idp', region_name='us-west-1')

def signup(username,password,email):
    try:
        # Sign up the user
        response = client.sign_up(
            ClientId='12o0nfiv0epben0n2goo3c8k27',
            Password=password,
            Username=username,
             UserAttributes=[
                {'Name': 'email', 'Value':email },
                {'Name': 'phone_number', 'Value': username}
            ]
        )
        
        return response['UserSub']
    except client.exceptions.UsernameExistsException:
        return False
    except Exception as e:
        return str(e)
    


def authenticate_user(username,password):
    try:
        # Initiate the authentication flow
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
        ClientId='12o0nfiv0epben0n2goo3c8k27'

        )

        # Extract the authentication result
        authentication_result = response
        # If successful, return the access token
        return True

    except client.exceptions.NotAuthorizedException as e:
        print("Invalid username or password:", e)
        return None

    except client.exceptions.UserNotFoundException as e:
        print("User not found:", e)
        return None
