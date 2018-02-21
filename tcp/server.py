#!/usr/bin/python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port your service
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while(True):
    c, addr = s.accept()    # Establish a connection with client.
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()               # Close the connection

