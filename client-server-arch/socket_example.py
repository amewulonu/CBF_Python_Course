import socket

HOST = 'www.google.com'
PORT = 80

socket = socket.socket()
socket.connect((HOST, PORT))

# Send an HTTP GET request to request the page
socket.send(b"""
GET / HTTP/1.1
Host: www.google.com

""")
msg = socket.recv(8192)
socket.close()
print(msg)