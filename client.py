import socket

class Client():
   def __init__(self,Address=('149.125.140.242',5000)):
      self.s = socket.socket()
      self.s.connect(Address)

c = Client()