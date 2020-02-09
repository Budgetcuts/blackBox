import socket
import sys
from requests import get

server_ip = get('https://api.ipify.org').text

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

      while True:
      # Wait for a connection
         print('waiting for a connection')
         connection, client_address = sock.accept()

         try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
               data = connection.recv(16)
               print('received "%s"' % data)
               if data:
                  print('sending data back to the client')
                  connection.sendall(data)
               else:
                  print('no more data from', client_address)
                  break

         finally:
            # Clean up the connection
            connection.close()

s = server()
s.update_ip(server_ip)
s.server_start()