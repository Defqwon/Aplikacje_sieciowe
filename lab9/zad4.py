import socket

address = 'httpbin.org'
port = 80

req = 'POST /post HTTP/1.1\r\n' \
      'Host: httpbin.org\r\n' \
      'Content-Length: 114\r\n' \
      'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36\r\n' \
      'Content-Type: application/x-www-form-urlencoded\r\n\r\n' \
      'custname=viktar&custtel=12345678&custemail=viktar@mail.gg&size=large&topping=onion&delivery=fffff&comments=hello!&\r\n'

if __name__ == '__main__':
    try:
        file = open('zadanie4.json', 'w')

        socket_conn = socket.create_connection((address, port))
        socket_conn.sendall(req.encode('utf-8'))

        response = b''
        buffer = socket_conn.recv(1024)
        while buffer:
            response += buffer
            buffer = socket_conn.recv(1024)

        response_str = response.decode('utf-8')

        header_end_index = response_str.index('\r\n\r\n') + 4
        headers = response_str[:header_end_index].split('\r\n')
        body = response_str[header_end_index:]

        content_length = 0
        for header in headers:
            if header.startswith('Content-Length'):
                content_length = int(header.split(': ')[1])

        json_data = body[:content_length]

        file.write(json_data)
        file.close()

        socket_conn.close()

    except socket.error as e:
        print('Error occurred while connecting to the server: {}'.format(e))
