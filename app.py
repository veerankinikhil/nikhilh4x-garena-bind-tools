#!/usr/bin/env python3
import os
import server

# WSGI Application adapter for gunicorn app:app
def app(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    if path == '/' or path == '/index.html':
        if os.path.exists(server.HTML_FILE):
            with open(server.HTML_FILE, 'rb') as f:
                content = f.read()
            start_response('200 OK', [
                ('Content-Type', 'text/html; charset=utf-8'),
                ('Content-Length', str(len(content))),
                ('Access-Control-Allow-Origin', '*')
            ])
            return [content]
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return [b'Not Found']

if __name__ == "__main__":
    server.run_server()
