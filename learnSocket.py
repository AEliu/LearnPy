from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 8000))

doc = []
while True:
    l = s.recv(1024)
    doc.append(l)
    print(l)
    if not l:
        break
print(doc)
