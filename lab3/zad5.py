import socket

UDP_IP = '212.182.24.27'
UDP_PORT = 2901
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input('Wpisz wiadomość: ')
    client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))
    data, server_address = client_socket.recvfrom(1024)
    print('Otrzymano od serwera:', data.decode())

client_socket.close()