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
        print(words[2])
        counts[words[2]] = counts.get(words[2],0) + 1
    else:
        continue
print(counts)

