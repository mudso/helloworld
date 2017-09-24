number = 23
running = True
while running:
    guess = int(input('enter an integer : '))
    if guess == number:
        print('Congratulations , you guessed it.')
        print('but you do not win any prizes')
        running = False
    elif guess < number:
        print('no,it is a little higher than that')
    else:
        print('no,it is a little lower than that')
else:
    print('the while loop is over')
print('done')