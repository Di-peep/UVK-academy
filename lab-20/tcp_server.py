import socket


SERVER_ADDR = ('localhost', 9595)


def run_tcp_server():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(SERVER_ADDR)
    server.listen(1)
    print('Waiting for connection...')

    conn, addr = server.accept()
    print(f'Connection: {addr}')

    msg = 1
    while msg:
        try:
            msg = conn.recv(64)
            print(f'msg: {msg.decode()}')
            conn.send('Message is received'.encode())
        except Exception as err:
            print(f'Error: {err}')
            conn.close()
            break


if __name__ == '__main__':
    run_tcp_server()
