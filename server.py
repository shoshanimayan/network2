#import socket module
from socket import *
from threading import Thread
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
#Fill in start
serverPort=1200
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
#Fill in end
while True:
# Establish the connection
    print ("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        outputdata = f.read()
#Send one HTTP header line into socket
#Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
#Fill in end
#Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()
    except IOError:

#Send response message for file not found
#Fill in Start
        connectionSocket.send(bytes(b"HTTP/1.1 404 Not Found\r\n\r\n"))
#Fill in end
#Close client socket
#Fill in start
        connectionSocket.close()
#Fill in end
    serverSocket.close()
