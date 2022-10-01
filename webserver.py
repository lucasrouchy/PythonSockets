from distutils.ccompiler import new_compiler
import socket
import sys
s = socket.socket()
host = int(sys.argv[1])
port = 9999
s.bind(('', host))
maxConnections = 10
s.listen(maxConnections)
print(f'Listening on port {host}')

# ch = []
while True:
    new_conn = s.accept()
    print(new_conn)
    new_socket = new_conn[0]
    data = new_socket.recv(4096)
    print(data.decode("ISO-8859-1"))
    ht = b"""\
HTTP/1.1 200 OK

Hello, World, Welcome to my server of DOOM!
"""
    if new_socket == "\r\n\r\n":
        break
    new_socket.sendall(ht)
    new_socket.close






