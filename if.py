number = 23
guess = int(input('Enter an integer : '))#将字符串转换成一个整数
if guess == number:
    print('Congratulations , you guessed it.')
    print('but you do not win any prizes')
elif guess < number:
    print('no,it is a little higher than that')
else:
    print('no,it is a little lower than that')

print('done')