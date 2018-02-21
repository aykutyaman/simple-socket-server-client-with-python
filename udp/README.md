UDP client-server

The UDP works differently from TCP/IP. Where TCP is a stream oriented, ensuring that all of the data
is transmitted in the right order, UDP is message oriented protocol.
UDP does not require a long-lived connection, so setting up a UDP socket is a little simpler. On the
other hand, UDP messages must fit within a single datagram and delivery is not guaranteed as it is with
TCP.

```
# Following would start a server in background.
$ python3 server.py &

# Once server is started run client as follows:
$ python3 client.py
```