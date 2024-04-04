from flask import Flask, request, jsonify
app = Flask(__name__)
import secrets
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json
app.config['JWT_SECRET_KEY'] = json.dumps(secrets.SystemRandom().getrandbits(128))

jwt = JWTManager(app)
from flask_cors import CORS, cross_origin
CORS(app)
import boto3
from DB import saveUser
from Authenticate import signup
from Authenticate import authenticate_user
from DB  import getItems


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    if not data or 'phoneNumber' not in data or 'password' not in data:
        return jsonify({'error': 'phoneNumber and password are required'}), 400

    username = data['phoneNumber']
    password = data['password']
    email=data['email']
    response=signup(username,password,email)
    if response is False:
            return jsonify({'error': 'Username already exists'}), 201

    # Create a new user
    else:
        saveUser(username,email)
        return jsonify({'message': 'User registered successfully'}), 200



@app.route('/authenticateUser', methods=['POST'])
def authenticateUser():
    data = request.json
    print("data",data)
    phoneNumber = data['phone']
    password = data['password']
    if not data or 'phone' not in data or 'password' not in data:
        return jsonify({'error': 'phoneNumber and password are required'}), 400
    response=authenticate_user(phoneNumber,password)
    if response is None:
            return jsonify({'error': 'Login failed,invalid phone or password' }), 400

    # Create a new user
    else:
        accessToken = create_access_token(identity=phoneNumber)
        print("accessToken",accessToken)
        return jsonify({'accessToken': accessToken}), 200


@app.route('/data', methods=['GET'])
def get_data(): 
    device_id = request.args.get('deviceId')
    startTime = request.args.get('startTime')
    endTime=request.args.get('endTime')
    response=getItems(device_id,startTime,endTime)
    return json.dumps(response)

