#作品名称：Pyinfo信息数据库
#版本：v1.1.0
#更新说明：增加基本交互式功能
#GiHub上的作者：bobby233
#说明：这个数据库可以管理任何你可以想到的数据管理。比如学生信息，分数信息等等。

#这是一个大的数据库
#这是一个例子，冒号前面的叫键，后面的叫值，值和键都可以随意更改。
"""info = {'bobby': {'first': 'John',
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
        print('YOU CANNOT CHANGE THE INFO!')   #不是管理员，不可以修改信息"""

#未来可能做的：1.添加注册功能    2.添加普通用户    3.指定查看一人的信息

###############################新代码###########################################
#版本：v2.0.0beta
#更新说明：重写大部分代码，实现永久添加，修改和删除。
#         唯一的遗憾，数据库格式变了，存储的信息少了。
"""重要说明：如果想体验新版本，请注释新代码分割线上方的所有代码，请使用三个英文引号进行注释，
            就像这个注释一样。"""
import json

message = ''
message_bak = ''
login = 'Hi, please log in to start(type "q" at anytime to quit).\nType your username: '
password = 'Type your password: '
do = 'What do you want to do? '
info_fn = 'info.json'
creat_info = 'You can creat an info box.\nType the name(key): '
creat_value = 'Type the info(value): '
info = {}
info_success = 'You creat an info box successfully. Please close the app.'
to_creat = 'You need to creat an info box.\nYou can type "creat"'
in_key = 'You can add(or change) name(key) and info(value).\nType the name(key): '
in_value = 'Type the info(value): '
add_success = 'You add(or change) the name(key) and info(value) seccessfully!'
out_key = 'You can delete name(key) and info(value).\nType the name(key): '
del_success = 'You delete the name(key) and info(value) successfully!'
help_list = ['see: see all info',
             'creat: creat an info box',
             'add: add or change sth into the info box',
             'delete: delete sth in the info box',
             'help: see the help',
             'price: see the price of the future products',
             '',
             'If you want more helps, add QQ2370706289(the developer) to get answer.']
price_list = ['Pyinfo Classic(this product): free',
              'Pyinfo Pro: CN￥0.9',
              'Pyinfo Pro_CN: CN￥1',
              'Pyinfo Online: CN￥6',
              'Pyinfo Online_Pro: CN￥9',
              'Pyinfo Online_Pro_CN: CN￥10',
              '',
              'Pybot: free',
              'Pybot Max: CN￥19',
              'Pybot Online: CN￥20',
              'Pybot Infinite: CN￥29',
              '',
              'For more prices, add QQ2370706289(the developer) to get answer.']

while message != 'q':
    message = input(login)
    if message == 'admin':   #用户名不建议修改
        message = input(password)
        if message == '0518':   #密码可以修改
            while message != 'q':
                message = input(do)

                #功能see：查看所有人的信息
                if message == 'see':
                    #检测是否创建数据库
                    try:
                        with open(info_fn) as infos:
                            info = json.load(infos)
                    except FileNotFoundError:
                        #如果没有就去creat一个
                        print(to_creat)
                    else:
                        #如果有就输出信息
                        for k, v in info.items():
                            print('Here is the info about ' + k + ':')
                            print(v)
                            
                #功能creat：创建一个数据库
                elif message == 'creat':
                    #检测是否有数据库
                    try:
                        with open(info_fn) as infos:
                            info = json.load(infos)
                    except FileNotFoundError:
                        #如果没有就创建一个
                        message = input(creat_info)
                        message_bak = input(creat_value)
                        info[message] = str(message_bak)
                        with open(info_fn, 'w') as infos:
                            json.dump(info, infos)
                        print(info_success)
                        break
                    else:
                        print('You do not need to creat an info box!')

                #功能add：添加（或更改）指定键和值
                elif message == 'add':
                    #检测是否有数据库
                    try:
                        with open(info_fn) as infos:
                            info = json.load(infos)
                    except FileNotFoundError:
                        #如果没有就creat一个
                        print(to_creat)
                    else:
                        #如果有就提示输入键和值来添加（或更改）
                        message = input(in_key)
                        message_bak = input(in_value)
                        info[message] = str(message_bak)
                        with open(info_fn, 'w') as infos:
                            json.dump(info, infos)
                        print(add_success)

                #功能delete：删除指定的键和值
                elif message == 'delete':
                    #检测是否有数据库
                    try:
                        with open(info_fn) as infos:
                            info = json.load(infos)
                    except FileNotFoundError:
                        #如果没有就creat一个
                        print(to_creat)
                    else:
                        #如果有就提示输入键和值来删除
                        message = input(out_key)
                        del info[message]
                        with open(info_fn, 'w') as infos:
                            json.dump(info, infos)
                        print(del_success)

                #帮助help：提示所有可用的命令
                elif message == 'help':
                    for help_item in help_list:
                        print(help_item)

                #报价price：查看目前或未来的产品价格
                elif message == 'price':
                    for item_price in price_list:
                        print(item_price)
                
        else:
            print('PASSWORD ERROR!!!')
    else:
        print('YOU CANNOT CHANGE THE INFO!')
