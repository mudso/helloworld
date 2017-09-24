import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url =' http://py4e-data.dr-chuck.net/known_by_Loulou.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count'))+1
position = int(input('Enter position')) - 1
tags = soup('a')
n = 0
while n < count:
    n = n + 1
    print( 'Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href', None)