import socket

server_address = ('212.182.24.27', 2902)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    number1 = input("Wpisz pierwszą liczbę: ")
    operator = input("Wpisz operator (+, -, *, /): ")
    number2 = input("Wpisz drugą liczbę: ")
    message = f"{number1} {operator} {number2}"
    sock.sendto(message.encode(), server_address)

    try:
        response, address = sock.recvfrom(1024)
        print(f"Port {server_address[1]} jest otwarty. Wynik: {response.decode()}")
    except socket.timeout:
        print(f"Port {server_address[1]} jest zamknięty.")

finally:
    sock.close()