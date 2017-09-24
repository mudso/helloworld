import urllib.request,urllib.error,urllib.parse
import sqlite3
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('urllibrary.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Urlname
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , rows INTEGER , cols INTEGER , url TEXT)''')

url = 'https://vincentarelbundock.github.io/Rdatasets/datasets.html'
urldata = urllib.request.urlopen(url,context = ctx).read()
#print(urldata)
soup = BeautifulSoup(urldata, 'html.parser')
#print(soup)
urld = list()
part = list()

tag1 = soup('td')
for tag in tag1:
    nStr=''
    a=tag.contents[0]
    nStr = nStr.join(a)
    nStr = nStr.replace('\n','').strip()
    part.append(nStr)
del part[0]

name = part[2::7]
row = part[3::7]
col = part[4::7]

tags = soup('a')
for tag in tags:
    a = tag.get('href', None)
    urld.append(a)
urld2 = urld[0::2]
print(urld2)

for i in range(len(name)):
    try:
        a,b,c,d = 0
        print(name[i], row[i],col[i],urld2[i])
        a = str(name[i])
        b = int(row[i])
        c = int(col[i])
        d = str(urld[i])
        cur.execute('''INSERT INTO Url(name,rows,cols,url) VALUES (?,?,?,?)''', (a, b, c, d))
        conn.commit()
    except:
        cur.execute('INSERT INTO Url(name,rows,cols,url) VALUES (?,?,?,?)', (a, b, c, d))
        conn.commit()
        continue

conn.commit
