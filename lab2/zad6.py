import socket

server_address = ('212.182.24.27', 2902)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    number1 = input("Wpisz pierwszą liczbę: ")
    operator = input("Wpisz operator (+, -, *, /): ")
    number2 = input("Wpisz drugą liczbę: ")
    message = f"{number1} {operator} {number2}"
    sock.sendto(message.encode(), server_address)
    response, address = sock.recvfrom(1024)
    print(f"Wynik: {response.decode()}")

finally:
    sock.close()