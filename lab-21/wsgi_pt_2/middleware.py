from wsgi_pt_2.api.middleware import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):
    """
    The simple middleware that logs every access to `/secured` endpoint.
    """
    def process_request(self, req):
        if req.path == '/secured':
            print(f'Log request: {req.path} => from {req.client_addr}')
