import socket

from tcp_server import SERVER_ADDR


def run_client():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(SERVER_ADDR)

    msg = 1
    while msg:
        msg = input('msg: ')
        try:
            client.sendto(msg.encode(), SERVER_ADDR)
            response = client.recv(64)
            print(response.decode())
        except Exception as err:
            print(err)
            break


if __name__ == '__main__':
    run_client()
