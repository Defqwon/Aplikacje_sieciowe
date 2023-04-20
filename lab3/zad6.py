import socket

UDP_IP = '212.182.24.27'
UDP_PORT = 2902

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

num1 = input('Wpisz pierwszą liczbę: ')
operator = input('Wpisz operator (+, -, *, /): ')
num2 = input('Wpisz drugą liczbę: ')
message = f'{num1} {operator} {num2}'
client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))
data, server_address = client_socket.recvfrom(1024)
print('Otrzymano od serwera:', data.decode())
client_socket.close()