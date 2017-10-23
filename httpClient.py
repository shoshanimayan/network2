import http.client
from sys import argv
if(len(argv) != 2):
    print("Usage: <httpclient.py> <url>")
    exit(1)
conn = http.client.HTTPConnection('localhost',12000)
conn.request("GET", "/" + argv[1])
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)

