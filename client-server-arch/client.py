import socket

HOST = "127.0.0.1"   # localhost
PORT = 4040

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send a message
message = "Hello from the Python client!"
client_socket.sendall(message.encode("utf-8"))

# Close the socket
client_socket.close()