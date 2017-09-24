import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""
countwords = dict()
while True:
    data = mysock.recv(1500)
    if (len(data) < 1): break
    time.sleep(0.1)
    count = count + len(data)
    if count <= 3000:
        words = data.split()
        for word in words:
            countwords[word] = countwords.get(word, 0) + 1
        print(data)
        print(len(data), count)

    picture = picture + data
print(countwords)
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
#Change your socket program so that it counts the number of characters it has received and stops displaying any text
# after it has shown 3000 characters. The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the document.