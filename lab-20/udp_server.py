import socket


SERVER_ADDR = ('localhost', 9595)


def run_udp_server():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.bind(SERVER_ADDR)
    print('Waiting for messages...')

    while True:
        try:
            msg, addr = server.recvfrom(64)
            print(f'from: {addr} -> {msg.decode()}')
            server.sendto('Message is received'.encode(), addr)
        except Exception as err:
            print(f'Error: {err}')
            break


if __name__ == '__main__':
    run_udp_server()
