import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('212.182.24.27', 2907)
hostname = input("Podaj nazwę hosta: ")
client_socket.sendto(hostname.encode(), server_address)
ip_address, address = client_socket.recvfrom(1024)
print("Adres IP dla hosta", hostname, "to", ip_address.decode())
client_socket.close()