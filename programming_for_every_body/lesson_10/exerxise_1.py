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
        a_name = words[1]
        counts[a_name] = counts.get(a_name,0) + 1
    else:
        continue

print(counts)
a = sorted([(v,k) for k,v in counts.items()])
a = sorted(a,reverse=True)
for k ,v in a:
    print(v,k)
