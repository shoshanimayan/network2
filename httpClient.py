from socket import *
import http.client

serverName = 'localhost'
serverPort = 80

#clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket.connect((serverName,serverPort))

conn = http.client.HTTPSConnection("localhost",serverPort)
conn.connect()
conn.request("GET", hR)
response = conn.getresponse()
data = response.read()
print (data)
conn.close()
