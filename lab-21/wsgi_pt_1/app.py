from wsgiref.simple_server import make_server

from wsgi_pt_1.api import (
    App,
    FirstMiddleware,
    SecondMiddleware
)


app = FirstMiddleware(SecondMiddleware(App()))


def run_server():
    try:
        server = make_server('localhost', 8000, app=app)
        print('> Server is running..')
        server.serve_forever()
    except KeyboardInterrupt:
        print('-! Server is stopped.')


if __name__ == '__main__':
    run_server()
