import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl

cxt = ssl.create_default_context()
cxt.check_hostname = False
cxt.verify_mode = ssl.CERT_NONE
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_27671.xml',context = cxt).read()
tree = ET.fromstring(url)
print(len(url))
counts = tree.findall('.//count')
st = 0
time = 0
for count in counts:
    num = int(count.text)
    st += num
    time +=1
print(time)
print(st)