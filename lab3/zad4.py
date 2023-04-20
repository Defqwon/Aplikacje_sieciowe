import socket

UDP_IP = '212.182.24.27'
UDP_PORT = 2901
MESSAGE = 'Hello, server!'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data, server_address = client_socket.recvfrom(1024)
print('Otrzymano od serwera:', data.decode())

client_socket.close()