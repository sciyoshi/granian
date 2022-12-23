import json


def info(environ, protocol):
    protocol(
        "200 OK",
        [('content-type', 'application/json')]
    )
    return [json.dumps({
        'scheme': environ['wsgi.url_scheme'],
        'method': environ['REQUEST_METHOD'],
        'path': environ["PATH_INFO"],
        'query_string': environ["QUERY_STRING"],
        'headers': {k: v for k, v in environ.items() if k.startswith("HTTP_")}
    }).encode("utf8")]


def echo(environ, protocol):
    print(environ)
    protocol(
        '200 OK',
        [('content-type', 'text/plain; charset=utf-8')]
    )
    return [environ['wsgi.input']]


def err_app(environ, protocol):
    1 / 0


def app(environ, protocol):
    return {
        "/info": info,
        "/echo": echo,
        "/err_app": err_app
    }[environ["PATH_INFO"]](environ, protocol)