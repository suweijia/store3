# class waterCup:
#     hight=20
#     broom=600
#     color="黑色"
#     stuff="不锈钢"
#
#     def store(self):
#         print("一个{}cm高，容积为{}毫升{}{}的水杯".format(self.hight,self.broom,self.color,self.stuff))
#
# cu=waterCup()
# cu.hight=25
# cu.broom=700
# cu.color="银灰色"
# cu.stuff="sus不锈钢材质"
# cu.store()

class Notebook:
    __screen=""
    __money=0
    __cpu=""
    __cont=""
    __time=""

    def setscreen(self,screen):
        self.__screen=screen
        print(screen,"的电脑可以敲代码".format(screen))
    def getscreen(self):
        return  self.__screen

    def setmoney(self,money):
        self.__money=money
        print("这个电脑",money,"元")
    def getmoney(self):
        return self.__money

    def setcpu(self,cpu):
        self.__cpu=cpu
        print(cpu,"的可以玩游戏")
    def getcpu(self):
        return self.__cpu

    def setcont(self,cont):
        self.__cont=cont
        print("{}:不错的内存".format(cont))
    def getcont(self):
        return self.__cont

    def settime(self,time):
        self.__time=time
        print("待机时间：",time)
    def gettime(self):
        return self.__time

    def cmd(self):
        print("{}-{}元-{}-{}的电脑可以敲码，打游戏，看视频".format(self.__screen, self.__money, self.__cpu, self.__cont))

cm=Notebook()
cm.setscreen("1920x1920pi")
cm.setmoney(5600)
cm.setcpu("麒麟芯片")
cm.setcont("16G")
cm.settime("12小时")
cm.cmd()

