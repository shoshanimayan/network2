import http.client
from sys import argv
if(len(argv) != 4):
    print(argv)
    print("Usage: httpclient.py <server_host> <server_port> <filename>")
    exit(1)
url = argv[1]+":"+argv[2]
print (url)
conn = http.client.HTTPConnection(argv[1], int(argv[2]))
#lab1
conn.request("GET", "/" + argv[3])
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
#lab2
conn.request("GET", "/lab2.html")
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
print(data1)
print(data2)
