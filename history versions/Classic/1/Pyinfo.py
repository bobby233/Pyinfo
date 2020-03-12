#作品名称：Pyinfo信息数据库
#版本：v1.1.0
#更新说明：增加基本交互式功能
#GiHub上的作者：bobby233
#说明：这个数据库可以管理任何你可以想到的数据管理。比如学生信息，分数信息等等。

#这是一个大的数据库
#这是一个例子，冒号前面的叫键，后面的叫值，值和键都可以随意更改。
info = {'bobby': {'first': 'John',
                  'last': 'Song',
                  'code name1': 'bobby',
                  'code name2': 'qswre3',
                  'grade': 7,
                  'class': 1,
                  'hight': 175,
                  'weight': 50,
                  'foot': 41,
                  'id': '310xxxxxxxxxxxxxxx'}}

#一个空信息来做动态提示
message = ''
#这是开始的提示，提示您登录
start = 'Hi, please log in to start.\nType your username: '
#并输入密码
typepassword = 'Type your password: '
#如果输入正确，出现欢迎
welcome = 'Welcome, admin!\nWhat do you want to do? '

while message != 'quit':
    #开始登录
    message = input(start)
    if message == 'admin':   #用户名可以修改
        message = input(typepassword)
        if message == '0518':   #密码也可以修改
            while message != 'quit':
                message = input(welcome)
                #登录成功

                #功能see：查看所有人的信息
                if message == 'see':
                    for name, infos in info.items():
                        print('\nThis is the info about ' + name + ':')
                        for k, v in infos.items():
                            print(k + ': ' + str(v))
        else:
            print('PASSWORD ERROR!!!')   #密码错误，登录失败
    else:
        print('YOU CANNOT CHANGE THE INFO!')   #不是管理员，不可以修改信息

#未来可能做的：1.添加注册功能    2.添加普通用户    3.指定查看一人的信息
