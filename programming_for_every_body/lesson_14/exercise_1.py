import urllib.request,urllib.parse,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_27672.json'
data = urllib.request.urlopen(url , context = ctx)
datas = json.load(data)
count = 0
sum = 0
for b in datas['comments']:
    count+=1
    sum += int(b['count'])
print(count,sum)
