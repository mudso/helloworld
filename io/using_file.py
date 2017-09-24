poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python'''

#打开文件以编辑（'w'riting)
f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    #因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()