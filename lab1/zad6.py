import sys
import socket

server_address = sys.argv[1]
server_port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_address, server_port))
    print("Połączono z serwerem")
except ConnectionRefusedError:
    print("Nie udało się połączyć z serwerem")
finally:
    client_socket.close()
