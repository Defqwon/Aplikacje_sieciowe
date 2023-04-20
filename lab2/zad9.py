import socket

server_address = ('212.182.24.27', 2906)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_address = input("Podaj adres IP: ")
client_socket.sendto(ip_address.encode(), server_address)
data, server = client_socket.recvfrom(1024)
print(f"Adres IP {ip_address} odpowiada hostowi o nazwie: {data.decode()}")
client_socket.close()