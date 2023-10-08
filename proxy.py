
import SimpleWebSocketServer
import SimpleHTTPSServer
import urllib


class JustAProxy(SimpleHTTPSServer.SimpleWebSocketServer):
      def do_GET(self):
         url=self.path[1:]
         self.send_response(200)
         self.end_headers()
         self.copyfile(urllib.urlopen(url), self.wfile)
         
if __name__ == '__main__':
   port = 25299
   httpd = SimpleWebSocketServer.SimpleWebSocketServer('localhost',port,JustAProxy)
   print ("Proxy Server at" , str(port))
   httpd.serveforever()

   
      
   
   
   
   
   
   
   
