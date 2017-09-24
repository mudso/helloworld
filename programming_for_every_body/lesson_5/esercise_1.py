total = 0
count = 0
average = 0
a = 0
while a == 0:
    u_number = input('Enter a nuber')
    if u_number == 'done':
        print(total)
        print(count)
        if  total/count:
            average = total / count
            print(average)
        else:
            print(average)
        break
    else:
        try :
            u_number = float(u_number)
        except:
            print('bad data')
            continue
        total = total + u_number
        count = count + 1
