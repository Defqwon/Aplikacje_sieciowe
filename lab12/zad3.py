import socket
import threading
import random
import numbers

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))

    def listen(self):
        self.sock.listen(5)

        print(f"Server started on {self.ip}:{self.port}")

        while True:
            client, address = self.sock.accept()

            print(f"Client {address[0]}:{address[1]} connected")

            client.settimeout(60)

            threading.Thread(target=self.client_handler,
                             args=(client, address)).start()

    def client_handler(self, client, address):
        server_random = self.generate_random_number(1, 50)

        print(f"Server random number = {server_random} for {address[0]}:{address[1]} client")

        while True:
            try:
                data = self.receive_data(client)

                if not data:
                    print(f"Connection {address[0]}:{address[1]} was closed on client side")
                    break

                client_number = self.parse_integer(data)

                if isinstance(client_number, numbers.Integral):
                    server_answer = self.process_guess(client_number, server_random)

                    self.send_data(client, server_answer)

            except socket.error as e:
                print(e)
                client.close()
                return False

    def generate_random_number(self, min_value, max_value):
        return random.randint(min_value, max_value)

    def parse_integer(self, data):
        try:
            return int(data.decode('utf-8'))
        except ValueError:
            error_message = f"{data.decode()} -> is not an integer!"
            self.send_data(client, error_message.encode())
            print(error_message)

    def process_guess(self, client_number, server_random):
        if client_number == server_random:
            return "You win!"
        elif client_number > server_random:
            return "Too much!"
        else:
            return "Too little!"

    def receive_data(self, client):
        buffer = b''
        while b'\r\n\r\n' not in buffer:
            buffer += client.recv(1)
        return buffer

    def send_data(self, client, data):
        client.send(data.encode())

if __name__ == "__main__":
    Server("127.0.0.1", 2900).listen()
