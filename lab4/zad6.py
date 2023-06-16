import socket

def server_program():
    host = "127.0.0.1"
    port = 2901

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started on {}:{}".format(host, port))

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        hostname = data.decode()

        try:
            ip_address = socket.gethostbyname(hostname)
            answer = "IP address for {} is: {}".format(hostname, ip_address)
        except socket.gaierror:
            answer = "IP address for {} is not found".format(hostname)

        server_socket.sendto(answer.encode(), client_address)

    server_socket.close()
    print("Connection closed on server side")


server_program()