import socket

HOST = '212.182.24.27'
PORT = 2908

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
message = input("Wpisz wiadomość: ")

if len(message) < 20:
    message += ' ' * (20 - len(message))

elif len(message) > 20:
    message = message[:20]

sock.sendall(message.encode())
data = sock.recv(1024)
print("Odpowiedź serwera:", data.decode())
sock.close()
