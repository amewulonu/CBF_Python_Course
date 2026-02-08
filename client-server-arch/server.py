import socket

HOST = "127.0.0.1"   # localhost
PORT = 4040

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to address and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(1024)

# Decode bytes to string and print
print("Message received:", data.decode())

# Close the connection
conn.close()
server_socket.close()