import socket

TCP_IP = '212.182.24.27'
TCP_PORT = 2900

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((TCP_IP, TCP_PORT))

while True:
    message = input('Wpisz wiadomość: ')
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print('Otrzymano od serwera:', data.decode())

client_socket.close()