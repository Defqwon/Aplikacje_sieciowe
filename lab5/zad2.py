import random
import numbers
import socket

host = '127.0.0.1'
port = 2965


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))
    server_socket.listen(10)

    print(f"Server started on {host}:{port}")

    while True:
        client_connected, client_address = server_socket.accept()

        print("Connection from: " + str(client_address))

        server_random = random.randint(1, 50)

        while True:
            print(f"Server random number: {server_random}")

            data = client_connected.recv(1024)

            if not data:
                print(f"Connection {client_address} was closed on client side")
                break

            try:
                client_number = int(data.decode())

                if client_number == server_random:
                    server_answer = "You win!"
                elif client_number > server_random:
                    server_answer = "Too much!"
                else:
                    server_answer = "Too little!"

                client_connected.send(server_answer.encode())

                if server_answer == "You win!":
                    server_socket.shutdown(socket.SHUT_RDWR)
                    server_socket.close()
                    print("Server closed")
            except ValueError:
                client_connected.send(f"{data.decode()} -> is not an integer!".encode())
                print(f"{data.decode()} -> is not an integer!")

        client_connected.close()


server_program()