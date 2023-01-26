import inspect
from urllib.parse import parse_qs

from parse import parse
from webob import Request, Response

from wsgi_pt_2.api.middleware import BaseMiddleware


class App:
    def __init__(self):
        self.routes = {}
        self.middleware = BaseMiddleware(self)

    def __call__(self, environ, start_response):
        return self.middleware(environ, start_response)

    def add_middleware(self, middleware_cls):
        self.middleware.add(middleware_cls)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request: Request):
        response = Response()

        try:
            handler_data, kwargs = self.find_handler(request.path)
            if handler_data:
                handler = handler_data['handler']
                allowed_methods = handler_data['methods']

                if inspect.isclass(handler):
                    handler = getattr(handler(), request.method.lower(), None)

                if handler is None:
                    raise AttributeError("Method not allowed", request.method)

                if request.method not in allowed_methods:
                    raise AttributeError("Method not allowed", request.method)

                handler(request, response, **kwargs)
            else:
                self.set_response(response)

        except AttributeError:
            self.set_response(response, 405, 'Method not allowed.')

        return response

    def add_route(self, path, handler, methods=None):
        """
        If path already exists in the routes,
        then the handler will be rewritten.
        """
        if not methods:
            methods = ['GET']

        self.routes[path] = {
            'handler': handler,
            'methods': methods
        }

    def route(self, path, methods=None):
        def wrapper(handler):
            self.add_route(path, handler, methods)
            return handler

        return wrapper

    @staticmethod
    def set_response(
            response,
            code=404,
            type_='text/html',
            text='Page not found.',
            body=b''
    ):
        response.status_code = code
        response.content_type = type_
        response.text = text
        response.body = body

    @staticmethod
    def handle_query_string(request: Request):
        return parse_qs(request.query_string)
