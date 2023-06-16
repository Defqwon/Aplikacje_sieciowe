import socket

address = 'httpbin.org'
port = 80

req = 'GET /html HTTP/1.1\r\n' \
      'Host: httpbin.org\r\n' \
      'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36\r\n' \
      'Accept: text/html\r\n\r\n'


def receive_response(sock):
    response = b''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data
    return response.decode('utf-8')


if __name__ == '__main__':
    try:
        file = open('zadanie1.html', 'w')

        with socket.create_connection((address, port)) as sock:
            sock.sendall(req.encode('utf-8'))
            response = receive_response(sock)

        header_end_index = response.index('\r\n\r\n') + 4
        headers = response[:header_end_index].split('\r\n')
        body = response[header_end_index:]

        content_length = 0
        for header in headers:
            if header.startswith('Content-Length'):
                content_length = int(header.split(': ')[1])

        html = body[:content_length]

        file.write(html)
        file.close()

    except socket.error as e:
        print('Error occurred while connecting to the server: {}'.format(e))
