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

target = 'X-DSPAM-Confidence:'
count = 0
count_number = 0
for line in fhand:
    if target in line :
        location = line.find(':')
        number = float(line[location+1:-1])
        count += 1
        count_number = number + count_number
        #print(line)
print(count)
print(count_number)
print(count_number/count)