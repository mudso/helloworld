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
        rdata = words[5]
        rhour = rdata[:3]
        counts[rhour] = counts.get(rhour,0) + 1
    else:
        continue
a = list(counts.items())
a.sort()
print(a)


#a = sorted([(k,v) for k,v in counts.items()])
#print(a)
#for k ,v in a:
#    print(k,v)
