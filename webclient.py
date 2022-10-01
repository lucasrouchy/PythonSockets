import socket
import sys
website = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket()
host = 'example.com'
ht = f"GET / HTTP/1.1\r\nHost: {website}\r\nConnection: close\r\n\r\n"
encodedht = ht.encode("ISO-8859-1")

s.connect((f"{website}", port))
s.sendall(encodedht)
o = s.recv(4096)
de = o.decode("ISO-8859-1")
print(de)
if len(o) == 0:
    s.close()