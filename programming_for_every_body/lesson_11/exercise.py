import re
re_exp = input('please input a reguler expression:')

fopen = open('mbox.txt')
counts = 0
for line in fopen:
    if re.search(re_exp,line):
        counts += 1
print('mbox.txt had {} lines that matched {}'.format(counts,re_exp))