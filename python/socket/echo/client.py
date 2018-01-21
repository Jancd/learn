#!/usr/bin/env python3

import socket 

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s :
    s.connect((HOST,PORT))
    s.sendall(b'Hello socket!!')
    data = s.recv(1024)
    print(data)

# $ python client.py
# b'Server reply :Hello socket!!'
