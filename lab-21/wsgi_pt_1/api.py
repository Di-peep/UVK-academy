class App:
    def __call__(self, environ, start_response):
        response_status = '200 OK'
        response_headers = [
            ('Content-Type', 'text/plain')
        ]
        response_body = '\n'.join([
            f'{key}: {value}' for key, value in environ.items()
        ])

        start_response(response_status, response_headers)
        return [response_body.encode()]

    # def __call__(self, environ, start_response):
    #     response_body = b"Hello, World!"
    #     status = "200 OK"
    #     start_response(status, headers=[])
    #     return iter([response_body])


class FirstMiddleware:
    """
    The simple middleware that prints the username,
    remote address, user agent, path and your surname.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        environ_filtered = self._filter(environ)
        app_response = self.app(environ_filtered, start_response)
        return [data for data in app_response]

    @staticmethod
    def _filter(env: dict):
        expected_keys = ['USERNAME', 'REMOTE_ADDR', 'HTTP_USER_AGENT', 'PATH_INFO']
        new_env = dict(filter(lambda couple: couple[0] in expected_keys, env.items()))
        new_env['SURNAME'] = 'VIHOR'
        return new_env


class SecondMiddleware:
    """
    The simple middleware that changes the formatting of all
    the symbols to be lowercase.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        handle_environ = self._handle_environ(environ)
        app_response = self.app(handle_environ, start_response)
        return [data for data in app_response]

    @staticmethod
    def _handle_environ(env: dict):
        new_env = dict(map(lambda t: (t[0], t[1].capitalize()), env.items()))
        return new_env
