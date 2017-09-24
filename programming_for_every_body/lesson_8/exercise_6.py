fname = input('please input a file name>')
try:
    lines = open(fname,'r')
except:
    print('bad name')
useful_address = 0
bad_address = 0
for line in lines:
    words = line.split()

    if len(words) != 0 and words[0] == 'From':
        print(words[1])
        useful_address += 1
    else:
        bad_address += 1
print(useful_address)
print(bad_address)