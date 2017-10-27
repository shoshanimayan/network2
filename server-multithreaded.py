#import socket module
from socket import *
import _thread

def worker(conn, addr):
    try:
        feed = b''
        message = ""
        byte_count = 0
        while(1):
            feed = conn.recv(1)
            message += feed.decode()
            byte_count += 1
            if(byte_count >= 4 and message[-4:] == "\r\n\r\n"):
                break
        filename = message.split()[1]
        with open(filename[1:], "rb") as f:
            outputdata = f.read()
            #Send one HTTP header line into socket
            conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
            #Send the content of the requested file to the client
            for i in range(0,len(outputdata)):
                conn.send(outputdata[i:i+1])
            conn.send(b'\r\n\r\n')
        conn.close()
    except IOError:
        #Send response message for file not found
        #Fill in Start
        conn.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
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
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    #Fill in end
    while True:
    # Establish the connection
        print ("Ready to serve...")
        connectionSocket, addr = serverSocket.accept()
        _thread.start_new_thread(worker, (connectionSocket, addr))

    serverSocket.close()

if __name__=="__main__":
    main()
