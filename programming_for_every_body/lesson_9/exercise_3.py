fname = input('please input a file name:')
try:
    fread = open(fname,'r')
except:
    print('bad name!!')
    quit()
counts = {}
for line in fread:
    words = line.split()
    if len(words) >0 and words[0]=='From':
        counts[words[1]] = counts.get(words[1],0) + 1
    else:
        continue
print(counts)

max = None
min = None
for k,v in counts.items():
    v = int(v)
    if max == None or v > max:
        max = v
        name = k
    else:
        continue
print(max)
print(name)

