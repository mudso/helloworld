import urllib.request,urllib.error,urllib.parse
import sqlite3
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('airpassenger2.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Air
        (id INTEGER PRIMARY KEY AUTOINCREMENT, time FLOAT , airpassenger INTEGER)''')



url = 'https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/AirPassengers.csv'
urldata = urllib.request.urlopen(url).read()
soup = BeautifulSoup(urldata, 'html.parser')
count = 0
data = []
for row in soup:
    row = row.replace('\n',',')
    words = row.split(',')
    for word in words:
        count += 1
        if count >= 4:
            data.append(word)
date = data[1::3]

air = data[2::3]
print(len(air))
for i in range(len(date)):
    print(i)
    d=float(date[i])
    e=int(air[i])
    cur.execute('INSERT INTO Air (airpassenger,time) VALUES ( ?,?)', (e,d))

conn.commit()

