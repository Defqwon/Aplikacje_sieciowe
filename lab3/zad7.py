import sys
import socket

if len(sys.argv) != 3:
    print("Usage: python client.py <server_address> <server_port>")
    sys.exit(1)

server_address = sys.argv[1]
server_port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_ip = socket.gethostbyname(server_address)
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)
    print("Connection established with server at", server_ip, "on port", server_port)

    service_name = socket.getservbyport(server_port)
    print("Service running on port", server_port, "is", service_name)

except socket.gaierror:
    print("Error: Invalid server address.")
    sys.exit(1)

except ConnectionRefusedError:
    print("Error: Connection refused by the server.")
    sys.exit(1)

client_socket.close()