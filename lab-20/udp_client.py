import socket

from udp_server import SERVER_ADDR


def run_client():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    msg = input('msg: ')
    while msg:
        try:
            client.sendto(msg.encode(), SERVER_ADDR)
            response = client.recv(64)
            print(response.decode())
        except Exception as err:
            print(f'Error: {err}')
            break
        else:
            msg = input('msg: ')


if __name__ == '__main__':
    run_client()
