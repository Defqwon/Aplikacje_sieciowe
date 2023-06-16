import socket
import threading

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
        while True:
            try:
                data = self.receive_data(client)
                if data:
                    print(f"Client {address[0]}:{address[1]} sent: {data}")
                    self.send_data(client, data)
                else:
                    raise socket.error("Client disconnected")
            except socket.error as e:
                print(e)
                client.close()
                return False

    def receive_data(self, client):
        buffer = b''
        while b'\r\n\r\n' not in buffer:
            buffer += client.recv(1)
        return buffer.decode('utf-8')

    def send_data(self, client, data):
        client.send(data.encode("utf-8"))


if __name__ == "__main__":
    Server("127.0.0.1", 2900).listen()
