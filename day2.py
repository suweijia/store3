
import math

#温度转换程序
'''
#输入格式为：22C

Tempstr = input("请输入带有符号的温度值：")

#定义一个Tempstr来存放用户输入的字符,input表示得到用户输入的东西

if Tempstr[-1] in ['F','f']:#表示判断Tempstr中的最后一个字符是否为这两个字符

#if是判断语句，判断语句的最后一个字符。

##Tempstr[-1]表示Tempstr的最后一个字符,这里用这个方法来判断是华氏度还是摄氏度。

    C = (eval(Tempstr[0:-1])-32)/1.8

#eval() 函数用来执行一个字符串表达式，并返回表达式的值

#去掉一对# 双引号或者一对单引号，然后以语句形式执行剩下的句子

#即为将任何字符串变成python语句

#Tempstr[0:-1]相当于获得除去最后一个字符的其余字符，可以理解为获得温度的数值

    print("转换后的摄氏温度是：{:.2f}C".format(C))#以 .2f 的格式输出C的值

#{}表示槽，将format函数得变量放入槽中

elif Tempstr[-1] in ['C','c']:

    F = 1.8*eval(Tempstr[0:-1])+32

    print("转换后的华氏温度是{:.2f}F".format(F))#以 .2f 的格式输出F的值
else:
    print("输入格式错误")
'''

#输入圆的半径计算计算周长和面积。

'''
while 1:
    radius1 = int ( input ("请输入圆的半径:") )
    #周长
    girth1 = 2 * radius1 * math.pi #圆周率
    #面积
    area1= radius1**2 * math.pi #
    print("此圆的周长为：",girth1)
    print("此圆的面积为：", area1)
else:
    print("请输入阿拉伯数字")
'''
#输入年份判断是不是闰年
'''
while 1:
    years1 = int (input("请输入年份："))
    if years1%4 == 0 and years1%100 != 0:
        print("是闰年")
    elif years1%400 == 0 :
        print("是闰年")
    else:
        print("不是闰年")
'''
#英制单位英寸与公制单位厘米互换
'''
while 1:
    lenght1= input(("单位换算-请输入带有“in”或“cm”单位的长度："))
    if lenght1[-2:] in ['cm']:
        inch = int(lenght1[0:-2])%2.54
    #lenght1[0:-2] 取lenght1字符串第一位到倒数第二位之前的字符
        print("厘米换算后的英寸长度为：{:.2f}in".format(inch))
    #format指定的是{:.2f},相当于inch{:.2f}   .2f到小数点后两位
    elif lenght1[-2:] in ['in']:
        cent = int(lenght1[0:-2])*2.54
        print("厘米换算后的英寸长度为：{:.2f}cm".format(cent))
    else:
        print("请按格式输入")
'''
#百分制成绩转换为等级制成绩。
'''
while 1:
    num1 = float(input("请输入成绩0~100之间："))
    if num1 >=90:
        print("A")
    elif  num1 <90 and num1 >= 80:
        print("B")
    elif  num1 <80 and num1 >= 70:
        print("C")
    elif  num1 <70 and num1 >= 60:
        print("D")
    elif  num1 <60 and num1 >= 0:
        print("E")
    else:
        print("请正常输入")
'''
#输入三条边长，如果能构成三角形就计算周长和面积
'''
print("输入三条边长，计算三角形周长和面积（默认单位是cm）")
while 1:
    side1 = float(input("请输入a边："))
    side2 = float(input("请输入b边："))
    side3 = float(input("请输入c边："))
    if side1+side2>side3 and side3+side2>side1 and side1+side3>side2:
        grith = side3+side2+side1
        area = 0.25*((side1+side2+side3)*(side1+side2-side3)*(side1-side2+side3)*(side3+side2-side1))**0.5
        print("三角形的周长是{},面积是{:.2f}".format(grith,area))
    else:
        print("输入有误，请重新输入")
'''
