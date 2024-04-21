import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())

finally:
    # Close the connection
    client_socket.close()