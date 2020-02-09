import socket
import sys

<<<<<<< HEAD
class Client():
   def __init__(self,Address=('149.125.140.242',5000)):
      self.s = socket.socket()
      self.s.connect(Address)
=======
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>>>>>> 35f686e35b090b5748ad4c8e136ccf4cb1ee6a89

ip = 'localhost' # change to yours

# Connect the socket to the port where the server is listening
server_address = (ip, 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    # Send data
    message = (b'This is the message.  It will be repeated.')
    print('sending "%s"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()