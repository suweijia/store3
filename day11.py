# import time
# class oldphone():
#     __conduct = ""  # 品牌
#     phonenum=""   #电话号码
#
#     def setConduct(self,conduct):
#         self.__conduct=conduct
#         print("你的{}手机挺不错".format(self.__conduct))
#     def getConduct(self):
#         return self.__conduct
#
#
#     def call(self,number):
#         print("{}手机{}正在给{}电话".format(self.__conduct,self.phonenum,number))
#
#
# class newphone(oldphone):
#
#     def call(self,number):
#         super().call(number)
#         print("语音拨号中",end="")
#         for i in range(5):
#             print(".",end="")
#             time.sleep(1)
#         print()
#         print("拨打成功")
#
#
#
# newso = newphone()
#
# newso.setConduct("华为")
# newso.phonenum="13531129768"
# newso.call("15031297505")

class chef:
    __name=""
    __age=0

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

    def srice(self):#蒸饭
        print("{}岁的{}正在蒸饭，用了1L的水和0.5L的米".format(self.setAge,self.setName))

class chefson(chef):#儿子

    def sfry(self):#炒菜
        print("{}岁的{}正在炒菜，做了西红柿炒鸡蛋，和干煸豆角".format(self.setAge,self.setName))

class chefgson(chefson):
    def srice(self):#孙子
        print("蒸饭",end=",")

    def sfry(self):
        # print("{}岁的{}在炒菜".format(self.age,self.name))
        print("炒菜")

class chefgsons(chefson):
    def srice(self):
        print(self.setAge)


ch=chefgson()
ch.srice()
ch.sfry()

csons=chefgsons()







