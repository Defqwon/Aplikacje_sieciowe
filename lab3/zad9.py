import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('212.182.24.27', 2906)
ip_address = input("Podaj adres IP: ")
client_socket.sendto(ip_address.encode(), server_address)
hostname, address = client_socket.recvfrom(1024)
print("Nazwa hosta dla adresu IP", ip_address, "to", hostname.decode())
client_socket.close()