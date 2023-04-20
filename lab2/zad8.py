import argparse
import socket

parser = argparse.ArgumentParser(description='Skaner portów TCP')
parser.add_argument('host', metavar='host', type=str,
                    help='adres serwera do przeskanowania')
args = parser.parse_args()

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "unknown"

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        print(f"Port {port} na serwerze {host} jest otwarty ({get_service_name(port)})")
    except:
        print(f"Port {port} na serwerze {host} jest zamknięty")
    finally:
        s.close()

for port in range(1, 65536):
    is_port_open(args.host, port)
