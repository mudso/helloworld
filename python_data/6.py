import requests
import re
from bs4 import BeautifulSoup
import time

pages = 1
counts = 0
star_counts = 0
sum = 0
while counts<50:
    r = requests.get('https://book.douban.com/subject/1003284/comments/hot?p={}'.format(pages))
    soup = BeautifulSoup(r.text,'html.parser')
    patterns = soup.find_all('p','comment-content')
    for pattern in patterns:
        counts += 1
        print(counts,'-',pattern.string)
        if counts==50:
            break
    pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
    #。当然，使用re.compile()函数进行转换后，re.search(pattern, string)的调用方式就转换为 pattern.search(string)的调用方式。
    p = re.findall(pattern_s, r.text)
    for star in p:
        star_counts += 1
        sum += int(star)
        if star_counts ==50:
            break
    time.sleep(5)
    pages += 1
print(sum/star_counts)


#1.	“迷你爬虫编程小练习”进阶：抽取某本书的前50条短评内容并计算评分的平均值。