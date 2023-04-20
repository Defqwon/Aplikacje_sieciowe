import socket

server_address = ('212.182.24.27', 2901)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    message = "Hello, world!"
    sock.sendto(message.encode(), server_address)

    response, address = sock.recvfrom(1024)
    print(response.decode())

finally:
    sock.close()