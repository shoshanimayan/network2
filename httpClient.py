import http.client
from sys import argv
if(len(argv) != 4):
    print(argv)
    print("Usage: httpclient.py <server_host> <server_port> <filename>")
    exit(1)
conn = http.client.HTTPConnection(argv[1], int(argv[2]))
conn.request("GET", "/" + argv[3])
r1 = conn.getresponse()
print(r1.status, r1.reason)
data = r1.read()
print(data)
