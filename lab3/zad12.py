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

total_sent = 0
while total_sent < len(message):
    sent = sock.send(message[total_sent:].encode())
    if sent == 0:
        raise RuntimeError("Połączenie zostało przerwane przez serwer")
    total_sent += sent

received = 0
response = b''
while received < 20:
    data = sock.recv(20 - received)
    if len(data) == 0:
        raise RuntimeError("Nie udało się odebrać całej wiadomości")
    received += len(data)
    response += data

print("Odpowiedź serwera:", response.decode())
sock.close()