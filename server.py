import socket

# defining the socket object

# Protocol family : AF_INET (IP version 4)
# Type of communication desired : reliable delivery stream service (TCP): SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding the socket
#bind function assigns an IP address and a Port number to a socket
# It is used when a socket has to be made a server socket
# The server program listens on published ports, hence it is required that an IP address and a port number
# is explicilty assigned to the server socket.
# We will host the server on the same machine on which we have our code, so we bind the 
# socket to the local host. We get it by the function gethostname()

#host name, port number
s.bind((socket.gethostname(), 1234))

#specifying a queue length for the server
s.listen(5)

#listen for the connections
while True:
    # client socket object, address of the client

    # s.accept() -> Waits for an incoming connection.
    # Returns a new socket representing the connection,
    # and the address of the client. 
    # For IP sockets, the address info is a pair (hostaddr, port).
    clientsocket, address = s.accept()

    print(f"Connection from {address} has been established")

    #send info to the client socket
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    clientsocket.close()