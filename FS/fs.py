###FS: Fibonacci Server:

#Importing Flask packages
from flask import Flask, request
from flask_api import status
import json #In order to load the sample Json Object as given in the question
from socket import *

#Creating instance of Flask Web Application
app = Flask(__name__)


#Defining how we are accessing the web page, so we need to provide the route.
@app.route('/fibonacci', methods = ['GET'])

#Providing Fibonnaci Value for a given Number:
def fibonacci():
    number = request.args['number']
    result = calculate_fibonacci_number(number)
    return str(result)

def calculate_fibonacci_number(number):
    number = int(number)
    if number <= 2:
        return 1
    return calculate_fibonacci_number(number-1) + calculate_fibonacci_number(number-2)

#Contains Name & IP address of the Fibonacci Server and IP Address of Authoritative Server
@app.route('/register', methods = ['PUT'])
def register():
    content = request.get_json()
    # print(content)
    hostname = content.get('hostname')
    ip = content.get('ip')
    as_ip = content.get('as_ip')
    as_port = int(content.get('as_port'))
    register_json = {'TYPE': 'A', 'NAME': hostname, 'VALUE': ip, 'TTL': 10}
    # print(register_json)
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.sendto(json.dumps(register_json).encode(), (as_ip, as_port))
    response_message, server_address = client_socket.recvfrom(2048)
    return 'successfully registered', status.HTTP_201_CREATED

#Running the Flask Application of Fibonacci Server on local host:
app.run(host='0.0.0.0',
        port=9090,
        debug=True)
