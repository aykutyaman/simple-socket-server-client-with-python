Multicasting client-server

Point-to-point connections handle a lot of communication needs, but passing the same information between
many peers becomes challenging as the number of direct connections grows. Sending messages separately to
each recipient consumes additional processing time and bandwith, which can be a problem for applications
such as streaming video and audio. Using multicast to deliver messages to more than one endpoint at a time achieves better efficiency because the network infrastructure ensures that the packets are delivered to all recipients.

Multicast messages are always sent using UDP, since TCP assumes a pair of communicating systems.

The addresses for multicast, called multicast groups, are a subset of regular IPv4 address range (224.0.0.0 through 230.255.255.255) reserved for multicast traffic. These addresses are treated specially by network routers and switches, so messages sent to the group can be distributed over the Internet to all recipients that have joined the group.

