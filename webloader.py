# Webloader 0.1 by EJ36

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests

console = "SERVER: "
print(console, "Welcome to WebLoader v0.1")


hostName = "localhost"
serverPort = 8080

url = input("Enter URL: ")


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #GETTER
        r = requests.get(url)
        #SETTER
        self.wfile.write(bytes(r.content))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), RequestHandler)
    print(console, "Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print(console, "WebLoader v0.1 shutting down.")
