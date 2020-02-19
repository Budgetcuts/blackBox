import socket
import sys
from requests import get

is_server_open = False

def get_ip():
   return get('https://api.ipify.org').text

def server_status():
   return is_server_open

server_ip = get_ip()

class server:
   def __init__(self):
      self.ip = 'localhost'

   def update_ip(self, new_ip):
      self.ip = new_ip

   def server_start(self):
      # Create a TCP/IP socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # Bind the socket to the port
      server_address = (self.ip, 10000)
      print('starting up on %s port %s' % server_address)
      sock.bind(server_address)

      # Listen for incoming connections
      sock.listen(1)

      msg = []

      while True:
      # Wait for a connection
         print('?? waiting for a connection')
         connection, client_address = sock.accept()

         try:
            print(':: connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
               full_msg = recombine_msg(msg)
               print("MSG: ", full_msg)

               if "<END>" in full_msg:
                  print("!! client terminated connection")
                  break

               data = connection.recv(16)
               msg.append(data)
               print(':: received "%s"' % data)
               if data:
                  print(':: sending data back to the client')
                  connection.sendall(data)
               else:
                  print('!! no more data from', client_address)
                  break
         finally:
            # Clean up the connection
            connection.close()
            print('!! closed connection')

def recombine_msg(msg):
   out = ""
   for m in msg:
      out += str(m[2:len(m)-1])
   return out

def start():
   print("STARTED SERVER FILE!")
   s = server()
   s.update_ip(server_ip)
   is_server_open = True
   s.server_start() # Commented out for testing gui