#用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
# 新用户可以用与现有系统帐号不冲突的用户名创建帐号，已存在的老用户则可以用用户名和密码登陆重返系统。
user_sys = {}
while True:
    name = input('please input a user name')
    passport = input('please input your passpore')

    if name in user_sys and user_sys[name] == passport :
        print('successful login')
    elif name not in user_sys:
        test = input('do you want to create this new account?')
        if test == 'y':
            user_sys[name] = passport
            print ('you creat a new account')
    print(user_sys)

