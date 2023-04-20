import socket

server_address = ('212.182.24.27', 2900)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(server_address)

    message = "Hello, world!"
    sock.sendall(message.encode())

    response = sock.recv(1024)
    print(response.decode())

finally:
    sock.close()