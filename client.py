import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The connect method connects a TCP based
# client socket to a TCP based server socket.
# The IP address of a server socket is passed
# as the parameter to the connect() method.
s.connect((socket.gethostname(), 1234))




#receiving the message from the server

full_msg = ''

while True:
    #buffersize
    msg = s.recv(10)
    if len(msg) <= 0:
        break
    
    full_msg += msg.decode("utf-8")
    
print(full_msg)
