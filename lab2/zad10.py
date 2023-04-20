import socket

server_address = ('212.182.24.27', 2907)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = input("Podaj nazwę hosta: ")
client_socket.sendto(hostname.encode(), server_address)
data, server = client_socket.recvfrom(1024)
print(f"Nazwa hosta {hostname} odpowiada adresowi IP: {data.decode()}")
client_socket.close()