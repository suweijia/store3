'''
创建类：用户，地址，银行，界面
账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、地址、存款余额(int)、开户行（银行的名称（str））写死的！
'''
import time
import random
import pymysql
from DBUtils import *

# 用户类
class User:
    __account = ""
    __name = ""
    __password = ""
    __address = None
    __money = 0
    __bank = "中国工商银行昌平支行"

    # 私有化属性
    def setAccount(self,account):
        self.__account = account
    def getAccount(self):
        return self.__account
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setPassword(self,password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money
    def getBand(self):
        return self.__bank

# 地址类
class Address:
    __country = ""
    __province = ""
    __street = ""
    __door = ""

    # 私有化属性
    def setCountry(self,country):
        self.__country = country
    def getCountry(self):
        return self.__country
    def setProvince(self,province):
        self.__province = province
    def getProvince(self):
        return self.__province
    def setStreet(self,street):
        self.__street = street
    def getStreet(self):
        return  self.__street
    def setDoor(self,door):
        self.__door = door
    def getDoor(self):
        return self.__door

# 工具类
class Tool:
    # 获取当前时间
    def getTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 根据用户名查询数据
    def getSelect(self,username):
        sql = "select * from user_bank where username=%s"
        param = [username]
        return select(sql, param)

    # 根据账号查询
    def getSelectAc(self,ac):
        sql = "select * from user_bank where account=%s"
        param = [ac]
        return select(sql, param)

    # 获取随机码
    def getRandom(self):
        li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
        string = ""
        for i in range(8):
            string = string + li[int(random.random() * len(li))]
        return string

    # 客户信息显示
    def getClientInfo(self,data):

        myinfo = '''
            \033[0;32;40m
            ------------账户信息------------
            账号：{account}
            姓名：{username}
            密码：{password}
            地址：
                国家：{country}
                省份：{province}
                街道：{street}
                门牌号：{door}
            账户余额：{money}
            注册银行名：{bank_name}
            -------------------------------
            \033[0m
        '''

        print(myinfo.format(account=data[0][0],
                            username=data[0][1],
                            password=data[0][2],
                            country=data[0][3],
                            province=data[0][4],
                            street=data[0][5],
                            door=data[0][6],
                            money=data[0][7],
                            bank_name=data[0][9]
                            ))

# 银行类
class Bank:

    # 创建类
    user = User()
    address = Address()
    tool = Tool()
    user2 = User()

    # 添加用户
    def bank_addUser(self):

        # 接收类里面的数据
        account = self.user.getAccount()
        username = self.user.getName()
        password = int(self.user.getPassword())
        country = self.user.getAddress().getCountry()
        province = self.user.getAddress().getProvince()
        street = self.user.getAddress().getStreet()
        door = self.user.getAddress().getDoor()
        money = self.user.getMoney()
        bank = self.user.getBand()

        # 查询是否已满
        sql = "select count(*) from user_bank"
        param = []
        data = select(sql, param)
        if data[0][0] >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from user_bank where username = %s"
        param1 = [self.user.getName()]
        data1 = select(sql1, param1)
        if len(data1) != 0:
            return 2

        # 插入数据
        else:
            sql2 = "insert into user_bank value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param2 = [account, username,password, country, province, street, door, money, self.tool.getTime(), bank]
            updata(sql2, param2)
            return 1
    def addUser(self):

        # 接收数据并添加到类里面
        self.user.setAccount(self.tool.getRandom())
        self.user.setName(input("用户名"))
        self.user.setPassword(input("密码"))
        self.address.setCountry(input("国家"))
        self.address.setProvince(input("省份"))
        self.address.setStreet(input("街道"))
        self.address.setDoor(input("门牌号"))
        self.user.setAddress(self.address)

        # 调用银行的开户方法完成开户操作  返回 1 2 3
        status = self.bank_addUser()

        # 判断1   2   3
        if status == 1:
            print("恭喜开户成功,以下是您的开户信息：")
            data = self.tool.getSelectAc(self.user.getAccount())
            self.tool.getClientInfo(data)
        elif status == 2:
            print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
        elif status == 3:
            print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")

    # 存钱
    def bank_saveMoney(self):

        # 获取账号和金额
        account = self.user.getAccount()
        money = self.user.getMoney()

        # 查询该账号是否存在数据库
        data = self.tool.getSelectAc(account)

        if len(data) != 0:
            sql = "UPDATE user_bank SET money = money+%s WHERE account = %s"
            param = [money, account]
            updata(sql, param)
            return True
        return False
    def saveMoney(self):
        self.user.setAccount(input("账号"))
        self.user.setMoney(int(input("存入的金额")))

        flag = self.bank_saveMoney()

        if flag:
            print("存储成功!")
        else:
            print("对不起，您的个人信息不存在！请先开户后再次操作！")

    # 取钱
    def bank_takeMoney(self):

        account = self.user.getAccount()
        password = self.user.getPassword()
        money = self.user.getMoney()

        data = self.tool.getSelectAc(account)

        if len(data) != 0:
            if data[0][2] == int(password):
                if data[0][7] < money:
                    return 3
                else:
                    sql = "UPDATE user_bank SET money = money-%s WHERE account = %s"
                    param = [money, account]
                    updata(sql, param)
                    return 0
            else:
                return 2
        else:
            return 1
    def takeMoney(self):
        self.user.setAccount(input("账户"))
        self.user.setPassword(input("密码"))
        self.user.setMoney(int(input("取出金额")))

        f = self.bank_takeMoney()

        if f == 1:
            print("改用户不存在！")
        elif f == 2:
            print("密码错误！")
        elif f == 3:
            print("取款金额不足！")
        elif f == 0:
            print("取款成功！")
            # bank_selectUser(account,password)

    # 转账

    def bank_transformMoney(self):

        # 获取数据
        outAc = self.user.getAccount()
        inAc = self.user2.getAccount()
        outPass = self.user.getPassword()
        outputmoney = self.user.getMoney()

        # 按账号查询
        data = self.tool.getSelectAc(inAc)

        # 取钱调用
        status = self.bank_takeMoney()

        if status == 1:
            return status
        elif status == 2:
            return status
        elif status == 3:
            return status
        elif status == 0:
            if len(data) != 0:
                sql = "UPDATE user_bank SET money = money+%s WHERE account = %s"
                param = [outputmoney, inAc]
                updata(sql, param)
                return 0
            else:
                sql = "UPDATE user_bank SET money = money-%s WHERE account = %s"
                param = [outputmoney, outAc]
                updata(sql, param)
                return 1
    def transformMoney(self):
        self.user.setAccount(input("转出的账号"))
        self.user2.setAccount(input("转入的账号"))
        self.user.setPassword(input("转出的密码"))
        self.user.setMoney(int(input("要转出的金额")))

        f = self.bank_transformMoney()

        if f == 1:
            print("转出或转入的账号不存在！")
        elif f == 2:
            print("输入密码错误！")
        elif f == 3:
            print("转账金额不足！")
        elif f == 0:
            print("转账成功！")

    # 查询

    def bank_selectUser(self):

        account = self.user.getAccount()
        password = self.user.getPassword()

        data = self.tool.getSelectAc(account)

        if len(data) != 0:
            if password == str(data[0][2]):
                self.tool.getClientInfo(data)
            else:
                print("用户密码错误！")
        else:
            print("该用户不存在！")

    def selectUser(self):
        self.user.setAccount(input("账号"))
        self.user.setPassword(input("密码"))

        self.bank_selectUser()

# 界面类
class Interface:
    bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
    # 打印界面
    def inter(self):

        print("***********************************\n"
        "*      中国工商银行账户管理系统       *\n"
        "***********************************\n"
        "*               选项              *")


        welcome_item = '''*              {0}.{1}             *'''

        keys = self.bank_choice.keys()
        for i in keys:
            print(welcome_item.format(i, self.bank_choice[i]))
        print("**********************************")
        choose = input("请输入你的选择：")
        return choose

    # 输入选择
    # def choose(self):

# 创建界面类,银行类
inter = Interface()
bank = Bank()

# 主程序
while True:
    # 接收界面类返回的数据
    chose = inter.inter()
    if chose  == "1":
        bank.addUser()
    elif chose == "2":
        bank.saveMoney()
    elif chose == "3":
        bank.takeMoney()
    elif chose == "4":
        bank.transformMoney()
    elif chose == "5":
        bank.selectUser()
    elif chose == "6":
        print("Bye,Bye您嘞！！！！")
        break
    else:
        print("不存在该选项，别瞎弄！")

