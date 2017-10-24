import http.client
from sys import argv
if(len(argv) != 3):
    print("Usage: <httpclient.py> <ip address> <port>")
    exit(1)

conn = http.client.HTTPConnection('localhost', 12000)
url = argv[1]+":"+argv[2]+"/lab1.html"
print(url)
conn.request("GET", "/" + argv[1]+":"+argv[2]+"/lab1.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
