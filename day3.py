# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
print("请输入十个数字求和")
sumH = 0
for i in range(1,11):
    nub = input("请输入第{}个数字：".format(i))
    if nub.isalpha() or nub.isspace(): #isalpha()判断字符串是否为字母
        while 1:
            nub = input("输入有误,请重新输入第{}个数字：".format(i))
            if nub.isalpha() == False:
                if nub.isspace() == False:
                    nub = float(nub)
                    sumH = sumH + nub
                    break
    else:
        nub=float(nub)
        sumH = sumH + nub
averageH = sumH/10
print("该十个数字的和为{},平均数为{}".format(sumH,averageH))
'''
# 使用random模块，如何产生 50~150之间的数
'''
import random
print(random.uniform(50,150))
# print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数
# print( random.random() )             # 产生 0 到 1 之间的随机浮点数
# print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
# print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数
'''
# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
print("输入三条边长，计算三角形周长和面积（默认单位是cm）")
side1 = float(input("请输入a边："))
side2 = float(input("请输入b边："))
side3 = float(input("请输入c边："))
if side1+side2>side3 and side3+side2>side1 and side1+side3>side2:
    if side1 == side2 == side3:
        print("是等边三角形")
    elif side1 == side2 != side3 or side1 == side3 != side2 or side3 == side2 != side1:
        print("是等腰三角形")
    elif side1**2==side2**2+side3**2 or side2**2==side1**2+side3**2 or side3**2==side2**2+side1**2:
        print("是直角三角形")
    else:
        print("是普通三角形")
else:
    print("不是三角形")
'''
# 使用+，-号实现两个数的调换
'''
numA=int(input("请输入数A="))
numB=int(input("请输入数B="))
numA=numA+numB
numB=numA-numB
numA=numA-numB
print("转换后A={},B={}".format(numA,numB))
'''
# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
name = 'root'
passwd = 'admin'
while 1:
    usr_name = input("用户名：")
    if usr_name == name:
        for i in range(3):
            usr_passwd = input("密码：")
            if usr_passwd == passwd:
               print("登陆成功")
               break
            else:
                if i<2:
                    print("密码输入错误，请重新输入")
                else:
                    print("三次密码输入错误，用户已被锁定")
    else:
        print("用户名输入错误，请重新输入")
'''
# 打印*三角形图
'''
for i in range(11):
    for j in range(0,10-i):
        print(end=" ")#end 不换行
    for k in range(10-i,10):
        print("*",end=" ")
    print("")
'''
# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？
'''
print("一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米")
hiW=0
for i in range(20):
    hiW = hiW + 3
    if hiW <= 20:
        hiW = hiW -2
        #print(hiW)
    else:
        print("青蛙在{}天能出来".format(i))
        break
'''
# 使用while循环实现NxN乘法表的打印。
'''
print("打印NxN乘法表")
numN = int(input("输入N:"))
H1 = 0
while H1 <= numN:
    H1 += 1
    H2=0
    while H2 <= numN:
        H2 += 1
        if H2 < H1:
            print("{}x{}={}".format(H2, H1, H1*H2), end=" ")
        elif H2 == H1:
            print("{}x{}={}".format(H2, H1, H1*H2))
'''
#编程实现99乘法表的倒叙打印
'''
print("99乘法表")
H1 = 10
while H1 > 0:
    H1 -= 1
    H2=1
    while H2 < 10:
        if H2 == H1:
            print("{}x{}={}".format(H2, H1, H1*H2))
        elif H2 < H1:
            print("{}x{}={}".format(H2, H1, H1*H2), end=" ")
        H2 += 1
        '''
# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
h1=1
h2 =1
for i in range(1,21):
    h1 = h2*i
    print("{} != {}".format(i,h1))
    h2 = h1
'''
# 1.添加计数打印功能 2.添加次数金币功能和锁定系统功能。
'''
import random
x = int(input("请输入随机范围最小值："))
y = int(input("请输入随机范围最大值："))
ran = random.randint(x,y)
print(ran)
cv = 500
count = int(input("请输入金币娱乐次数："))
sum = count * cv
print("本次娱乐预计消费",sum,"个金币，游戏开始！",'\n',"友情提示:随机范围为：","(",x,y,")")
num1 = int(input("猜一猜小艺给出的数字："))
sum -= 500
while count >= 0:
    if num1 == ran:
        count -= 1
        sum += 1000
        print("太棒了！你猜对啦！恭喜你获得1000个金币，本次结束后金币数量为：",sum,"可以开始下一轮游戏啦！")
        break
    elif num1 > ran:
        count -= 1
        sum -= 500
        print("输入的数大了！")
    elif num1 < ran:
        count -= 1
        sum -= 500
        print("输入的数小了!")

    num1 = int(input("继续耐心猜一猜小艺给出的数字哦！"))
    if count == 0 and num1 != ran:
        print("很遗憾本次金币已用完，游戏结束！")
    '''