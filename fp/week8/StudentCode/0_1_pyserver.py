#!/usr/bin/python
#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
    #   print the request
        # print (self.headers)
        # Send response status code
        self.send_response(200)


        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        with open ("hello.html", "r") as myfile:
          data = myfile.read()

        # Send file back to client
        # Write content as utf-8 data
        self.wfile.write(bytes(data, "utf8"))
        return

def run():
  print('starting server...127.0.0.1, 5000')
  # Server settings
  # To choose port 8080, or port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
