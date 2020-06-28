# Tiny concurrent server and client based on UDP.

The program is needed to demonstrate how the UDP works.

There're several parts of program:

- Client class
- Server class
- Utilities

Client class implements client side of application: it
initializes connection and sends datagram to server.
 
Server class implements server side of application: it
waits for data from clients, unpacks it and checks errors
using checksum.

Utilities is a file with third party programs: there's a function 
which constructs UDP-datagram.

Server and clients works in different threads. This helps to
make an interaction system similar to the real one.