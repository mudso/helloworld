import urllib.request as ur
import urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_27669.html'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = ur.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
print(soup)
tags = soup('span')

numbers = []
counts = 0
for tag in tags:
    print(tag.string)
    counts += 1
    numbers.append(int(tag.string))

print(sum(numbers))
print(counts)
print(sum(numbers)/counts)
total = 0
for span in tags:
    total = total + int(span.contents[0])
print(total)