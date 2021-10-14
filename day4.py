#人员数据库
#
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# pay_4 = 0
# age_4 = 0
# for i in range(len(names)):
#     pay_4 = pay_4 + names[i][-2]
#     age_4 = age_4 + int(names[i][1])
# pay_4 = pay_4/len(names)
# age_4 = age_4/len(names)
# print("每个人的平均薪资是{}￥，每个人的平均年龄是{}岁".format(pay_4,age_4))
# names.append(["刘备","45","男","220","alibaba",500,"30"])
# # names_add1 = input("新员工姓名：")
# # names_add2 = input("新员工年龄：")
# # names_add3 = input("新员工性别：")
# # names_add4 = input("新员工编号：")
# # names_add5 = input("新员工任职公司：")
# # names_add6 = int(input("新员工新资："))
# # names_add7 = input("新员工部门编号：")
# # names_H=[names_add1,names_add2,names_add3,names_add4,names_add5,names_add6,names_add7]
# # names.append(names_H)
# # print(names)
# n=0;m=0;u=0;t=0;y=0
# for k in range(len(names)):
#     #for l in range(len(names[1])):
#     n = names[k].count('男') + n
#     m = names[k].count('女') + m
#     u = names[k].count('50') + u
#     t = names[k].count('60') + t
#     y = names[k].count('10') + y
# print("公司男人有{}个，女人有{}个,'50'部门有{}个人,'60'部门有{}个人,'10'部门有{}个人".format(n,m,u,t,y))

#现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
#
# mark =[['罗恩',23,35,44],
#        ['哈利',60,77,68,88,90],
#        ['赫敏',97,99,89,91,95,90],
#        ['马尔福',100,85,90]]
# for i in range(0,len(mark)):
#     mark_add = mark[i][1:]
#     n = 0
#     for j in range(len(mark_add)):
#         n = n+ mark_add[j]
#     print("{}的总成绩为{}".format(mark[i][0],n))

#当输入是54321时，写出下面程序的执行结果
#
# num = int(input("请输入一个数："))
# while num !=0:
#     print(num%10)
#     num = num //10

#请对下列列表进行冒泡排序
#
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# for i in range(len(a)):
#     for j in range(len(a)-i-1):
#         if a[j] <= a[j+1]:
#             print(a)
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

#1、请循环遍历出所有的key
#2、请循环遍历出所有的value
# 3、请在字典中增加一个键值对,"k4":"v4"
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# print("dict:")
# for i in dict:
#     print(i,":",dict[i])
# dict["k4"]="v4"

#小明去超市购买水果，账单如下
infos = {'苹果':32.8,
        '香蕉': 22,
        '葡萄': 15.5}

#小明，小刚去超市里购买水果
#小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
#以姓名做key，value仍然是字典
#
# Friuts = {'苹果': 12.3,  # 水果和单价
#           '草莓': 4.5,
#           '香蕉': 6.3,
#           '葡萄': 5.8,
#           '橘子': 6.4,
#           '樱桃': 15.8}
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':0
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money':0
#     }
# }
# def money(name):
#     sum=0
#     for i,j in Friuts.items():          #一个可遍历的key/value 对。
#         for k,l in info[name]['fruits'].items():
#             if i==k:
#                 sum += j*l
#     return sum
# info['小明']['money']=money('小明')
# info['小刚']['money']=money('小刚')
# for i in info:
#     for j in info[i]:
#         print(i,":{}".format(info[i][j]))

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# 返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
# list1=[21,56,34,15,4,21,56,56,10,10,21,21,15,34,33,21]
# def list0():
#     list2 = list(set(list1))
#     dict1 = {}
#     for i in list2:
#         list1.count(i)
#         dict1[i] = list1.count(i)
#     return dict1
# print("list1:",list0())

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# name_l=['年龄','性别','编号','任职公司','薪资','部门编号']
# dict1={}
# for i in names:
#     dict1[i[0]] = i[1:]    #将names改成字典格式
#     dict2 = dict(zip(name_l, dict1[i[0]]))   #将dict1每个键的值（list）与name_l压缩成新的字典
#     for j in dict1:
#         dict1[j]=dict2  #修改dict1的每个键的值
# print(dict1)
