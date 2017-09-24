import re
fname = input
fopen = open('mbox.txt')
y = list()
total = 0
for line in fopen:
    line = line.rstrip()
    x = re.findall('^New .+: ([0-9]+)', line)
    if len(x)>0:
        print(x)
        y.append(x)
        total += float(x[0])

print(y)
print(len(y))
print(total/len(y))