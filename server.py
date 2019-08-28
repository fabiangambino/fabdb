from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path = os.getcwd() + "/views" + self.path
        if self.path == "/":
            path = os.getcwd() + "/views/index.html"
        print 'path' + path
        if os.path.exists(path) is True:
            with open(path) as f:
                test_html = f.read()
                self.wfile.write(test_html)
        else:
            print 'file does not exist'

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=8888)
