import http.client
from sys import argv
if(len(argv) != 3):
    print(argv)
    print("Usage: httpclient.py <ip address> <port> <requested page>")
    exit(1)
url = argv[1]+":"+argv[2]
print (url)
conn = http.client.HTTPConnection(argv[1], int(argv[2]))
conn.request("GET", "/lab1.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)

