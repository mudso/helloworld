fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print(fname)
    else:
        print(fname.upper())
        print('File cannot be opened:', fname)
    exit()


for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])

