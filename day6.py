import random
bank={}
bank_name="中国工商银行分行"
#传入参数添加到字典里面
def bank_add(swell,username,password,country,province,street,door):
    while 1:
        if swell in bank:#说明用户已存在
            return 2
        elif len(bank) >= 100:
            return 3
        else:
            bank[swell]={
                "姓名":username,
                "密码":password,
                "地址":{
                    "国家":country,
                    "省份":province,
                    "街道":street,
                    "门牌号":door},
                    "存款余额":0,
                "开户行":bank_name
            }
            return 1
        break
def useradd():
    while 1:
        swell = "".join(random.sample('0123456789', 8))
        username=input("请输入您的用户名")
        while 1:
            password=(input("请输入您的用户密码(只能为数字)"))
            if password.isdigit():
                password=int(password)
                break
            else:
                continue
        print("下面请输入你的详细地址")
        country=input("\t\t请输入您的国家")
        province=input("\t\t请输入您的省份")
        street=input("\t\t请输入您的街道")
        door=input("\t\t请输入您的门牌号")
        add=bank_add(swell,username,password,country,province,street,door)
        if add == 3:
            print("数据库已满请到其他银行开户")
        elif add ==2:
            print("请输入其他用户名")
        elif add== 1:
            print("开户成功,下面是你的详细信息")
            break

#存钱
def cunqian():
    while 1:
        sewll0 = input("用户账号：")
        password0 = int(input("密码："))
        money_acc = int(input("存取金额："))
        if sewll0 in bank.keys():
            if password0 == bank[sewll0].get('密码'):
                sum = money_acc + bank[sewll0].get('存款余额')
                bank[sewll0]['存款余额'] = sum
                print(bank)
            else:
                print("密码不对")
                continue
        else:
            print("账号不存在")
            continue


#取钱
def quqian():
    while 1:
        print("取款")
        sewll0=input("用户账号：")
        password0=int(input("密码："))
        money_sup=int(input("取出金额："))
        if sewll0 in bank.keys():
            if password0 == bank[sewll0].get('密码'):
                if money_sup <= bank[sewll0].get('存款余额'):
                    dif = bank[sewll0].get('存款余额') - money_sup
                    bank[sewll0]['存款金额'] = dif
                else:
                    print("余额不够")
                print(bank)
            else:
                print("密码不对")
                continue
        else:
            print("账号不存在")
            continue

#转账
def zhuan():
    while 1:
        swell0 = input("转出账号：")
        swell1 = input("转入账号")
        password0 = int(input("密码："))
        money_sup0 = int(input("转账金额："))
        if swell0 in bank.keys() and swell1 in bank.keys():
            if password0 == bank[swell0].get('密码'):
                if money_sup0 <= bank[swell0].get('存款余额'):
                    sumr = bank[swell1].get('存款余额') + money_sup0
                    difr = bank[swell0].get('存款余额') - money_sup0
                    bank[swell1]['存款金额'] = sumr
                    bank[swell0]['存款金额'] = difr
                else:
                    print("余额不够")
                print(bank)
            else:
                print("密码不对")
                continue
        else:
            print("账号不对")
            continue
#查询
def caxun():
    while 1:
        listuser=[]
        swell3=input("查询账号")
        password3=int(input("密码："))
        if swell3 in bank.keys():
            if password3 == bank[swell3].get('密码'):
                print("账号：{}".format(swell3))
                print("余额：{}元".format(bank[swell3].get('存款余额')))
                for ress in bank[swell3]['地址'].values():
                    listuser.append(ress)
                listuser0="".join(listuser)
                print("用户居住地址：{}".format(listuser0))
                print("开户行：{}".format(bank[swell3].get('开户行')))
            else:
                print("密码不对，无法打印")
                continue
        else:
            print("账号不对")
            continue
#调用功能
while 1:
    print("*"*40)
    print("*            中国工商银行                *")
    print("*            账户管理系统                *")
    print("*               V1.0                   *")
    print("*"*40)
    dict_xitonglist={1:'开户',2:'存钱',3:'取钱',4:'转账',5:'查询',6:'再见'}
    for key_xtl,vaule_xtl in dict_xitonglist.items():
        print("*{}.{}                                 *".format(key_xtl,vaule_xtl))
    print("*"*40)
    print("")
    # for business in dict_xitonglist.keys():
    work = int(input("请选择要办业务(输入数字)："))
    if work in dict_xitonglist.keys():
        print("ok")
        if work == 1:
            print("1、开户")
            useradd()
            print(bank)
            back0 = input("是否返回主界面（Y or N）：")
            if back0 == 'Y' or back0 == 'y':
                print("返回主界面中……")
                continue
            else:
                useradd()
        elif work == 2:
            print("2、存钱")
            cunqian()
            print(bank)
            back0 = input("是否返回主界面（Y or N）：")
            if back0 == 'Y' or back0 == 'y':
                print("返回主界面中……")
                continue
            else:
                useradd()
        elif work == 3:
            print("3、取钱")
            quqian()
            print(bank)
            back0 = input("是否返回主界面（Y or N）：")
            if back0 == 'Y' or back0 == 'y':
                print("返回主界面中……")
                continue
            else:
                useradd()
        elif work == 4:
            print("4、转账")
            zhuan()
            print(bank)
            back0 = input("是否返回主界面（Y or N）：")
            if back0 == 'Y' or back0 == 'y':
                print("返回主界面中……")
                continue
            else:
                useradd()
        elif work == 5:
            print("5、查询")
            caxun()
            print(bank)
            back0 = input("是否返回主界面（Y or N）：")
            if back0 == 'Y' or back0 == 'y':
                print("返回主界面中……")
                continue
            else:
                useradd()
        elif work == 6:
            print("再见")
            break
    else:
        print("错误")