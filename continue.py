while True:
    s = input('enter something : ')
    if s == 'quit':
        break
    if len(s)<3:
        print('too small')
        continue
    print('input is of sufficent length')