#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
import socket
import os.path

## For gets current using IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()
#print (ip)

## For gets this one file name prefix
path = os.path.basename(__file__)
portnum = (path.split(".")[0])
#print(path.split(".")[0])

## Show the contents
app = Flask(__name__)
@app.route('/')
def index():
    return "Backend okay :)<br>\r\nIP address: " + ip + "<br>\r\nPort: " + portnum + "\r\n"

## Let this one file name to be the port number
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=(portnum), debug=True)
