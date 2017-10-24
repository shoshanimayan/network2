import http.client
from sys import argv
if(len(argv) != 4):
    print("Usage: httpclient.py <ip address> <port> <requested page>")
    exit(1)

conn = http.client.HTTPConnection(argv[1], int(argv[2]))
conn.request("GET", "/" + argv[3])
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
