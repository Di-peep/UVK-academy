import json
from http.server import HTTPServer, BaseHTTPRequestHandler


SERVER_ADDR = ('localhost', 9595)


class MyServer(BaseHTTPRequestHandler):
    FORM_DATA = {}

    def set_response(self, status_code: int):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    @staticmethod
    def form_response():
        response = '<html><head><title>Get data</title></head><p>Form data:</p><body>'
        response += ''.join({f'<p>{field}: {value}</p>' for field, value in MyServer.FORM_DATA.items()})
        response += '</body></html>'
        return response

    @staticmethod
    def save_data(data: bytes):
        data_json = json.loads(data)
        MyServer.FORM_DATA = dict(data_json)

    def do_GET(self):
        self.set_response(status_code=200)
        response = self.form_response()
        self.wfile.write(bytes(response, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.save_data(post_data)
        self.set_response(status_code=200)


def run_http_server():
    server = HTTPServer(SERVER_ADDR, MyServer)
    print("Server started http://%s:%s" % SERVER_ADDR)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")


if __name__ == '__main__':
    run_http_server()
