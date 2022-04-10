from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return


""""
- if the request is correct and there are no problems: 2XX
- if the request is not correct or there is something wrong from client side: 4XX 404 403
- if the req/res are not correct or something wrong happened from server: 5XX 500
"""