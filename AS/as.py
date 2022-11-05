"""
Author - Rahul Sahu
Net ID - RKS448
N Number - 14924303
Date - Thu Oct 8 10:48:15 2022
"""


###AS: Authoritative Server: Authorization for User Server


from socket import *
import json

#port 53533 to accept the UDP Connection
server_port = 53533

serverSock = socket(AF_INET, SOCK_DGRAM)
serverSock.bind(('', server_port))
ip_map = {}


def get_request(query_message):
    message = json.loads(query_message.decode())
    ip = 'VALUE' in message

    if not ip:
        hostname = message['NAME']
        request_type = message['TYPE']
        return dns_query(hostname, request_type)
    else:
        hostname = message['NAME']
        ip = message['VALUE']
        request_type = message['TYPE']
        ttl = message['TTL']
        return register(hostname, ip, request_type, ttl)


#To return the IP adddress in a DNS Message of the form as given in register() function.
def dns_query(hostname, request_type):
    content = ip_map[request_type + ' ' + hostname]
    fs_ip = content['VALUE']
    return str(fs_ip).encode()


def register(hostname, ip, request_type, ttl):
    content = {'TYPE': request_type, 'NAME': hostname, 'VALUE': ip, 'TTL': ttl}
    key = request_type + ' ' + hostname
    ip_map[key] = content
    return json.dumps('').encode()

        
while True:
    query_message, addr = serverSock.recvfrom(2048)
    response_message = get_request(query_message)
    serverSock.sendto(response_message, addr)
