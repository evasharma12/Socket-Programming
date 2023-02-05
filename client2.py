#Buffering and streaming data
import socket

#defining a contant headersize
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The connect method connects a TCP based
# client socket to a TCP based server socket.
# The IP address of a server socket is passed
# as the parameter to the connect() method.
s.connect((socket.gethostname(), 1234))




#receiving the message from the server

while True:
    full_msg = ''
    new_msg = True

    while True:
        #buffersize
        #To accept headersize length(length of msg) plus other thins along with it (actual string)
        msg = s.recv(16)

        # When a new message comes, get the length of the message
        # and set new_msg as false
        if new_msg:
            #The message(msg) contains the length of string from 
            #index 0 to headersize
            print(f'new message length: {msg[:HEADERSIZE]}')
            #parsing into int
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        
        full_msg += msg.decode("utf-8")

        #The length of the full message should be equal to the headersize plus msglen
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg received")
            #string slicing
            #getting the string part in the message received from the server
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''


    print(full_msg)
