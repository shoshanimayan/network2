#Student 1 Name: Paul Grad
#Student 1 ID: 94574913
#Student 2 Name: Mayan Shoshani
#Student 2 ID: 15019784
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Connect to the local host (an EECS server, where this code should be executed)
mailserver = "localhost"
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
serverPort =25
clientSocket.connect((mailserver,serverPort))

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
# Fill in start
heloCommand = 'MAIL FROM: <pgrad@crystalcove.eecs.uci.edu>\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
heloCommand = 'RCPT TO: <pgrad@uci.edu>\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send DATA command and print server response.
# Fill in start
heloCommand = 'DATA\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '354':
    print('250 reply not received from server.')
# Fill in end
# Send message data.
# Fill in start
heloCommand = 'hi\r\n'
clientSocket.send(heloCommand.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
heloCommand = '.\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send QUIT command and get server response.
# Fill in start
heloCommand = 'QUIT\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '221':
    print('250 reply not received from server.')
# Fill in end
