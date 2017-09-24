import random

#游戏程序主体
def guess():
    con = True
    right_number = random.randint(0,100)
    a = 0
    b = 100
    user_number = int(input('please enter a number between {}-{}>--'.format(a,b)))
    while con:
        if  user_number < right_number :
            a = user_number
            print ('the true number between{}-{}'.format(a,b))
            user_number = int(input('please enter a number between {}-{}>--'.format(a, b)))

        elif user_number > right_number :
            b = user_number
            print('the true number between{}-{}'.format(a,b))
            user_number = int(input('please enter a number between {}-{}>--'.format(a, b)))
        else:
            print ('bingo')
            con_t = input('if you want to try anain? y/n')
            if con_t == 'y':
                right_number = random.randint(0, 100)
                a = 0
                b = 100
                user_number = int(input('please enter a number between {}-{}>--'.format(a, b)))
                con = True
            elif con_t == 'n':
                con = False
            else:
                break

guess()