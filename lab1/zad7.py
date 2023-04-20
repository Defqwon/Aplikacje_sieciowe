import sys
import socket

server_address = sys.argv[1]

try:
    server_ip = socket.gethostbyname(server_address)
except socket.gaierror:
    print("Nieprawidłowy adres serwera")
    sys.exit()

port_list = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]

for port in port_list:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)  
    result = client_socket.connect_ex((server_ip, port))
    if result == 0:
        print(f"Port {port}: otwarty")
    else:
        print(f"Port {port}: zamknięty")
    client_socket.close()
