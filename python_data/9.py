user_data = {}
def newusers():
    n_name = input('please input a new account')
    if n_name in user_data:
        n_name = input('please input a new account')
    else:
        n_passport = input('passport')
        user_data[n_name] = n_passport
def oldusers():
    n_name = input('please input your account')
    n_passport = input('please input your passport')
    if user_data[n_name] == n_passport:
        print(n_name, 'welcome back ')
    else:
        print('login incorrect')

def login():
    choice = input('''
             (N)ew User Login 
             (O)ld User Login
             (E)xit
                    ''')
    if choice == 'N':
        newusers()
    elif choice == 'O':
        oldusers()
    elif choice == 'E':
        quit()

if __name__ == '__main__':
    while True:

        login()