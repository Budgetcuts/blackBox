import socket 
import sys

class client:
    def __init__(self):
        self.ip = 'localhost'  # '149.125.140.242' #''localhost' # change

    def update_ip(self, new_ip):
        self.ip = new_ip

    def connect_to(self,ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #ip = '149.125.140.242' # change to yours

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

c = client()
c.connect_to('149.125.140.242')