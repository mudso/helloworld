
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://movie.douban.com/subject/10763928/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia')
fhand = open('exerciser3.txt', 'wb')
size = 0
count = dict()
while True:
    info = img.read(5120)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)
print (fhand[:3000])
for word in fhand[:3000]:
    count[word] = count.get(word,0) + 1
print(count)
print(size, 'characters copied.')
fhand.close()