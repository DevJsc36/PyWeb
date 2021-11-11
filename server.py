# PyWeb 0.1 by EJ36

import http.server
import socketserver

console = "SERVER: "
print(console, "Welcome to PyWeb v0.1")


HOSTNAME = "localhost"
PORT = 8000


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(console, "Server started http://%s:%s" % (HOSTNAME, PORT))
    httpd.serve_forever()


if __name__ == "__main__":
    try:
        socketserver.serve_forever()
    except KeyboardInterrupt:
        pass

    socketserver.server_close()
    print(console, "Pyweb v0.1 shutting down.")