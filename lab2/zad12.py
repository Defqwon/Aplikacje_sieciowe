import socket

HOST = '212.182.24.27'
PORT = 2908
MESSAGE_LENGTH = 20

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
message = input('Podaj wiadomość: ')
message = message[:MESSAGE_LENGTH].ljust(MESSAGE_LENGTH)
sent = client_socket.send(message.encode())

if sent != MESSAGE_LENGTH:
    print(f'Błąd wysyłania wiadomości: wysłano tylko {sent} z oczekiwanych {MESSAGE_LENGTH} bajtów.')
else:
    print(f'Wysłano wiadomość: {message}')

response = client_socket.recv(MESSAGE_LENGTH).decode()

if len(response) != MESSAGE_LENGTH:
    print(f'Błąd odbierania wiadomości: odebrano tylko {len(response)} z oczekiwanych {MESSAGE_LENGTH} bajtów.')
else:
    print(f'Odebrano odpowiedź: {response}')

client_socket.close()
