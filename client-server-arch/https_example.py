import socket
import ssl

HOST = "academy.codingblackfemales.com"
PORT = 443

# Create a normal TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap it with SSL/TLS
context = ssl._create_unverified_context()
secure_socket = context.wrap_socket(sock, server_hostname=HOST)

# Connect securely
secure_socket.connect((HOST, PORT))

# Send HTTP request (now encrypted)
secure_socket.sendall(b"""
GET HTTP/1.1
Host: academy.codingblackfemales.com
Connection: close

""")

response = secure_socket.recv(8192)
secure_socket.close()

# print(response[:500])
print(response)