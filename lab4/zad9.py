import socket

def check_answer(data_decoded):
    data_array = data_decoded.split(";")

    try:
        if data_array[2] == "60788" and data_array[4] == "2901" and data_array[6] == "programming in python is fun":
            return "TAK"
        else:
            return "NIE"

    except IndexError:
        return "BAD SYNTAX"


def server_program():
    host = "127.0.0.1"
    port = 2910

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started on {}:{}".format(host, port))

    while True:
        data, client_address = server_socket.recvfrom(1024)

        if not data:
            break

        result = check_answer(data.decode())

        server_socket.sendto(result.encode(), client_address)

    server_socket.close()

    print("Connection closed on server side")


server_program()