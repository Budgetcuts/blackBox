import socket

class Client():
   def __init__(self,Address=('localhost',5000)):
      self.s = socket.socket()
      self.s.connect(Address)

c = Client()