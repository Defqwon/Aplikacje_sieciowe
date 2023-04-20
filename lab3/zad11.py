import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('212.182.24.27', 2908)
client_socket.connect(server_address)

message = "Hello, server!"

if len(message) < 20:
    message = message.ljust(20)
elif len(message) > 20:
    message = message[:20]

client_socket.send(message.encode())
response = client_socket.recv(1024)
print("Response from server: ", response.decode())

client_socket.close()