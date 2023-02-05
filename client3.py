#sending and receiving object with Pickling


import socket
import pickle

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
    #making the full message in bytes (b)
    full_msg = b''
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

        
        full_msg += msg

        #The length of the full message should be equal to the headersize plus msglen
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg received")
            #string slicing
            #getting the string part in the message received from the server
            print(full_msg[HEADERSIZE:])

            #The loads method loads data from a byte string
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''


    print(full_msg)
