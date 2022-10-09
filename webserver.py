from distutils.ccompiler import new_compiler
import os as o
import socket
import sys

def recieveData(new_socket):
    data = b""
    while True:
        data += new_socket.recv(4096)
        
        if b"\r\n\r\n" in data:
            break
    return data
def parseStrip(data):
    # headerData = data.find(b"\r\n\r\n")
    lines = data.split("\r\n")
    firstLine = lines[0]
    words = firstLine.split()
    file = words[1]
    _, filename = o.path.split(file)
    ext = o.path.splitext(filename)[-1]
    print("<<<<<<<<<<",ext)
    return filename, ext
def chooseMIME(ext):
    return MIMEmap.get(ext)

    
    
s = socket.socket()
host = int(sys.argv[1])
MIMEmap = {".ico": "image/vnd.microsoft.icon", ".txt": "text/plain", ".html": "text/html", ".gif": "image/gif", ".pdf": "application/pdf", ".jpeg": "image/jpeg"}
s.bind(('', host))
maxConnections = 10
s.listen(maxConnections)
print(f'Listening on port {host}')

# ch = []
while True:
    new_conn = s.accept()
    print(new_conn)
    new_socket = new_conn[0]
    data = recieveData(new_socket)

    filename, ext = parseStrip(data.decode("ISO-8859-1"))
    
    res = chooseMIME(ext)
    # numOfBytes = ReadingFile(filename)
    
    
    try:
        with open(filename) as fp:
            data = fp.read()   # Read entire file
            bdata = data.encode("ISO-8859-1")
            numOfBytes = len(bdata)
            ht = 'HTTP/1.1 200 OK\r\n\
            Content-Type: {}\r\n\
            Content-Length: {}\r\n\
            Connection: close\r\n\r\n\
            {}'.format(res, numOfBytes, data)
            enht = ht.encode("ISO-8859-1")
            print(ht)
            new_socket.sendall(enht)

    except:
        print("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 13\r\nConnection: close\r\n404 not found")
    
    # print(data.decode("ISO-8859-1"))
    
    new_socket.close()
    
        




# ht = b"""\
    # HTTP/1.1 200 OK
    

    # Hello, World, Welcome to my server of DOOM!
    # """

