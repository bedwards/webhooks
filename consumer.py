from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(
            self.rfile.read(
                int(self.headers.get('Content-Length'))).decode('utf-8'))
        self.send_response(200)
        self.end_headers()


HTTPServer(('', 8001), Handler).serve_forever()
