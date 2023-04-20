import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python port_scanner.py <server_address>")
    sys.exit(1)

server_address = sys.argv[1]

try:
    socket.inet_aton(server_address)
except socket.error:
    server_ip = socket.gethostbyname(server_address)
else:
    server_ip = server_address

for port in range(1, 65536):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.1)

    try:
        server_address = (server_ip, port)
        result = client_socket.connect_ex(server_address)
        if result == 0:
            print("Port", port, "is open")
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"
            print("Service:", service)

    except socket.error:
        pass

    client_socket.close()