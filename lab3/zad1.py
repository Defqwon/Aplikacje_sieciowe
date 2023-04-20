import socket
import struct
import time

NTP_SERVER = "ntp.task.gda.pl"
NTP_PORT = 13
TIME1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(1.0)
data = b'\x1b' + 47 * b'\0'

try:
    response = client.sendto(data, (NTP_SERVER, NTP_PORT))
    data, address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= TIME1970
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)))
except socket.timeout:
    print('Przekroczono czas oczekiwania.')
finally:
    client.close()