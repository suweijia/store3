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
