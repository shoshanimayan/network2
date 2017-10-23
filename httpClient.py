import http.client
conn = http.client.HTTPConnection('localhost',12000)
conn.set_tunnel("http://169.234.54.57:6789/lab2.html")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)

