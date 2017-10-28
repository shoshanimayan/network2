#Student 1 Name: Paul Grad
#Student 1 ID: 94574913
#Student 2 Name: Mayan Shoshani
#Student 2 ID: 15019784
from socket import *
from sys import argv
serverAddress=argv[1]
serverPort=int(argv[2])
path=argv[3]
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

get_request=("GET /" + path + " HTTP/1.1\r\n\r\n").encode("utf-8")
clientSocket.send(get_request)
    
feed = b''
message = b""
while(1):
    feed = clientSocket.recv(1)
    if(feed == b""):
        break
    message += feed
print(message)
clientSocket.close()
