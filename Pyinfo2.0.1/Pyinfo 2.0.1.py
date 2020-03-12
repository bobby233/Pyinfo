#作品名称：Pyinfo信息数据库
#GitHub上的作者：bobby233
#作者QQ：2370706289
#版本：v2.0.1
#更新说明：重写大部分代码，实现永久添加，修改和删除。
#         唯一的遗憾，数据库格式变了，存储的信息少了。
#从beta的更新：消息全部转移至其他文件，修复bug更简单。
#未来可能做的：1.添加注册功能   2.添加设置settings
import json

from string import *

print(beta)
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