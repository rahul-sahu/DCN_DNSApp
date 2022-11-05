"""
Author - Rahul Sahu
Net ID - RKS448
N Number - 14924303
Date - Thu Oct 8 10:48:15 2022
"""

###US: User Server:

#Importing Flask Packages
from flask import Flask, request
import requests
from flask_api import status
from socket import *
import json

#Creating instance of Flask Web Application
app = Flask(__name__)


#Defining how we are accessing the web page, so we need to provide the route.
@app.route('/fibonacci', methods = ['GET'])


#Accept_request function Accpeting the 5 Parameters:

def accept_request():
    hostname = request.args['hostname'] 
    fs_port = request.args['fs_port']
    as_ip = request.args['as_ip']
    as_port = int(request.args['as_port'])
    number = request.args['number']
    # print(hostname)
    # print(fs_port)
    # print(as_ip)
    # print(as_port)
    # print(number)

    #Server would return HTTP Code if any of the above 5 parameters is missing.
    if hostname == '' or fs_port == '' or as_ip == '' or as_port == '' or number == '' or not number.isdigit():
        return 'bad format', status.HTTP_400_BAD_REQUEST

    #Server would return HTTP Code 200 for a successful Request
    fs_ip = query_authoritative_server(as_ip, as_port, hostname)
    real_add = 'http://' + fs_ip + ':' + fs_port
    dict_to_send_1 = {'number': number}
    result = requests.get(real_add + '/fibonacci', params=dict_to_send_1)
    return result.text, status.HTTP_200_OK


#Querying to Authoritative DNS Server since User Server does not know the IP Address of given hostname
def query_authoritative_server(as_ip, as_port, hostname):
    client_socket = socket(AF_INET, SOCK_DGRAM)
    query_json = {'TYPE': 'A', 'NAME': hostname}
    client_socket.sendto(json.dumps(query_json).encode(), (as_ip, as_port))
    ip_address, server_address = client_socket.recvfrom(2048)
    return ip_address.decode()


#Running the Flask Application of User Server on local host:
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
