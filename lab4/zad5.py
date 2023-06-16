import socket

def server_program():
    HOST = '127.0.0.1'
    PORT = 2901

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))

    print("Server started on {}:{}".format(HOST, PORT))

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        ip_address = data.decode()

        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            answer = "Hostname for {} is: {}".format(ip_address, hostname)
        except socket.herror:
            answer = "Hostname for {} is not found".format(ip_address)

        server_socket.sendto(answer.encode(), client_address)

    server_socket.close()
    print("Connection closed on the server side")


server_program()