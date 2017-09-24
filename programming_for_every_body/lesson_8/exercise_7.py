
numbers=[]
while True:
    number = input('please input a numver-->')
    if len(numbers)!= 0 and number == 'done':
        print('max number is', max(numbers))
        print('min number is ', min(numbers))
        print('there are {} numbers'.format(len(numbers)))
    else:
        try:
            number = float(number)
            numbers.append(number)
            continue
        except:
            print('wrong number')
            quit()