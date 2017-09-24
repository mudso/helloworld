import requests
import urllib.request
import requests
from bs4 import BeautifulSoup
import re

sum = 0
r = requests.get('https://book.douban.com/subject/1003284/comments/')
soup = BeautifulSoup(r.text, 'html.parser')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(type(item))
    print(item)
    print(type(item.string))
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
#。当然，使用re.compile()函数进行转换后，re.search(pattern, string)的调用方式就转换为 pattern.search(string)的调用方式。
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
print(sum)