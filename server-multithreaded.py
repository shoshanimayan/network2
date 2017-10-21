#import socket module
from socket import *
import thread

def worker(conn, addr):
    try:
        message = conn.recv(2048)
        filename = message.split()[1]
        with open(filename[1:], "rb") as f:
            outputdata = f.read()
            #Send one HTTP header line into socket
            conn.send("HTTP/1.1 200 OK\n")
            #Send the content of the requested file to the client
            for i in range(0,len(outputdata)):
                connectionSocket.send(outputdata[i:i+1])
            conn.send(b'\r\n\r\n')
            conn.close()
    except IOError:
        #Send response message for file not found
        #Fill in Start
        conn.send("HTTP/1.1 404 Not Found\n")
        #Fill in end
        #Close client socket
        #Fill in start
        conn.close()
        #Fill in end

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    #Fill in start
    serverPort = 12000
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    #Fill in end
    while True:
    # Establish the connection
        print ("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        thread.start_new_thread(worker, (connectionSocket, addr))

    serverSocket.close()

if __name__=="__main__":
    main()
