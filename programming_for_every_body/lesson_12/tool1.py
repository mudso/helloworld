import socket
import re

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
urlname = input('please input a url')
try:
    surlname = urlname.split('/')
    HOST = surlname[2]
    mysock.connect((HOST, 80))
    cmd = 'GET {} HTTP/1.0 \r\n\r\n'.format(urlname).encode()
    mysock.send(cmd)
except:
    print('you enter a bad name')
    quit()

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()