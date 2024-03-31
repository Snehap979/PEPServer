from flask import Flask, request, jsonify
app = Flask(__name__)
# users = []

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     if not data or 'username' not in data or 'password' not in data:
#         return jsonify({'error': 'Username and password are required'}), 400

#     username = data['username']
#     password = data['password']

#     # Check if the username already exists
#     if any(user['username'] == username for user in users):
#         return jsonify({'error': 'Username already exists'}), 400

#     # Create a new user
#     new_user = {'username': username, 'password': password}
#     users.append(new_user)
#     return jsonify({'message': 'User registered successfully'}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     if not data or 'username' not in data or 'password' not in data:
#         return jsonify({'error': 'Username and password are required'}), 400

#     username = data['username']
#     password = data['password']

#     # Check if the user exists and the password is correct
#     for user in users:
#         if user['username'] == username and user['password'] == password:
#             return jsonify({'message': 'Login successful'}), 200

#     return jsonify({'error': 'Invalid username or password'}), 401

# @app.route('/users', methods=['GET'])
# def get_users():
#     return jsonify(users), 200

# if __name__ == '__main__':
#     app.run(debug=True)



# import boto3

# # Initialize AWS Cognito client
# client = boto3.client('cognito-idp', region_name='us-west-1')

# def signup(username, password):
#     try:
#         # Sign up the user
#         response = client.sign_up(
#             ClientId='12o0nfiv0epben0n2goo3c8k27',
#             Password='Ycaps9999!',
#             Username='+16576267473',
#              UserAttributes=[
#                 {'Name': 'email', 'Value':'snehap97779@gmail.com' },
#                 {'Name': 'phone_number', 'Value': '+16576267473'}
#             ]

#         )
#         return response['UserSub']  # Return the user sub (unique identifier)
#     except client.exceptions.UsernameExistsException:
#         return 'Username already exists'
#     except Exception as e:
#         return str(e)

# # Example usage:
# username = 'example_user'
# password = 'example_password'
# result = signup(username, password)
# print(result)



import boto3

# Initialize DynamoDB client
dynamodb = boto3.client(
    'dynamodb',
    region_name='us-west-1',
    # aws_access_key_id='AKIATCKAM2M6EZWVAP3Q',
    # aws_secret_access_key='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'
)

def save_user_info(username, email, phone_number):
    try:
        # Save user information to DynamoDB
        response = dynamodb.put_item(
            TableName='pepdatabase',
            Item={
                'user_id':{'S':user_id},
                'username': {'S': username},
                'email': {'S': email},
                'phone_number': {'S': phone_number}
            }
        )
        return True
    except Exception as e:
        print("Error saving user info:", e)
        return False

# Example usage:
username = 'example_user'
email = 'example@example.com'
phone_number = '+1234567890'
user_id='1234abcd'
if save_user_info(username, email, phone_number):
    print("User information saved successfully")
else:
    print("Failed to save user information")






