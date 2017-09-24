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
        a_num = a_name.find('@')
        a_address = a_name[a_num+1:-1]
        counts[a_address] = counts.get(a_address,0) + 1
    else:
        continue
print(counts)



