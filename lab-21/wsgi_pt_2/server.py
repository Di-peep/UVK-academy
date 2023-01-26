from wsgiref.simple_server import make_server

from wsgi_pt_2.app import app


def run_server():
    try:
        server = make_server('localhost', 8000, app=app)
        print('> Server is running on http://localhost:8000')
        server.serve_forever()
    except KeyboardInterrupt:
        print('-! Server is stopped.')


if __name__ == '__main__':
    run_server()
