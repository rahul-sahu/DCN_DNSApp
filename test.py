"""
Author - Rahul Sahu
Net ID - RKS448
N Number - 14924303
Date - Thu Oct 8 10:48:15 2022
"""

import requests

# Preparing request for the Fibonacci Series

d_send = {"hostname": "fibonacci.com", "ip": "0.0.0.0", "as_ip": "0.0.0.0", "as_port": "53533"}

# Variable to store the IP
fs_ip = 'http://0.0.0.0'

# Variable for Port
fs_port = '9090'

# Variable for regsiter link
fs_link = '/register'

# Variable for complete address and the register link
fs_add = fs_ip + ':' + fs_port + fs_link
# print(fs_add)

# Request for Json Send
res = requests.put(fs_add, json=d_send)
print(res.text)


d_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 9}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=d_send)
print(res.text)

d_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 5}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=d_send)
print(res.text)

d_send = {'hostname': 'fibonacci.com', 'fs_port': '9090', 'as_ip': '0.0.0.0', 'as_port': '53533', 'number': 'X'}
us_ip = 'http://0.0.0.0'
us_port = '8080'
us_add = us_ip + ':' + us_port + '/fibonacci'
res = requests.get(us_add, params=d_send)
print(res.text)
