'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import  random
#商品
shop=[
    #     0      1
    ["刀🔪",999],#0
    ["斧子",200],#1
    ["👍",90000],#2
    ["coco",150],#3
    ["枸杞",900],#4
]
#初始化余额
money=random.randint(0,99999)
print(money)
#购物车
mycart=[]
#轮盘概率
list_9=[0.9]
list_5=[0.5]
list_1=[0.1]
list_0=[0]
list_10=[1]
list0=list_9*50+list_5*10+list_1*3+list_0+list_10*36
list1=list_9*100+list_5*30+list_1*8+list_0*2+list_10*60
#展示商品
while False==0:
    discount0 = random.choice(list0)
    print("恭喜您获得{}折优惠".format(discount0*10))
    for index,value in enumerate(shop):
        print(index,":",value)
    chose=input("请输入商品编号")
    discount1 = random.choice(list1)
    print("恭喜您获得{}折优惠".format(discount1 * 10))
    if chose.isdigit():#str判断引号内是否为数字
        chose=int(chose)#转换成整型
        if chose <len(shop):#判断输入的内容是否小于列表的长度
            shop_m= shop[chose][1] * discount0 * discount1
            if money>shop_m:#判断money是否大于商品的价格
                mycart.append(shop[chose])#把商品加入购物车
                money=money-shop_m#money减去商品的价格
                print("恭喜你成功加入购物车，您的余额为：",money)
                # tt=input("是否继续购买（Y or N）：")
                # if tt == 'Y' or tt =='y':
                #     print()
                # elif tt == 'N' or tt =='n':
                #     print("=================")
                #     for index, value in enumerate(mycart):
                #         print(index, ":", value)
                #     print("您的余额为：", money)
                #     break
            else:
                print("gun")
        else:
            print("没有此商品")
    elif chose == "q" or chose == "Q":
        print("=================")
        for index, value in enumerate(mycart):
            print(index, ":", value)
        print("您的余额为：", money)
        break
    else:
        print("别瞎弄")
