def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    result = environ["QUERY_STRING"].split('&')
    return ["\n".join(result)]