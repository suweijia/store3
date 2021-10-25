import xlrd
from decimal import Decimal, ROUND_HALF_UP#四舍五入

sl = xlrd.open_workbook(filename=r"E:\狼腾\python自动化\day07\任务\2020年每个月的销售情况.xls",encoding_override=True)
#读取整个工作表sheet文件名
sh = sl.sheet_names()
print(sh)
#data = sh[1].cell_value(0,1)定位单元格   print(data)
#获取某个sheet文件内容
def sheet_mo(month):
    shm= sl.sheet_by_name(sh[month])
    return shm
# sheet_mo(1)   >>>Sheet  1:<2月>
#data= st.row_values(i) 打印每列

#全年的销售总额
sal_sum=0

for i in range(len(sh)):
    rows = sheet_mo(i).nrows  # 获取多少行
    for xin in range(1,rows):
        data = sheet_mo(i).row_values(xin)
        sal_sum =sal_sum + Decimal(data[2]).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP) * Decimal(data[4]).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)
print("全年的销售总额:",sal_sum,"元")


xiaoshou_0=0
pinpai=[]
xiaoshoui={}
shz={}#每月初始字典
for i in range(len(sh)):
    shz[sh[i]]=0


for i in range(len(sh)):
    rows = sheet_mo(i).nrows  # 获取多少行
    for xin in range(1, rows):
        data = sheet_mo(i).row_values(xin)#获取列表
        xiaoshou_0 = xiaoshou_0 + data[4]#全年销售总量
        if data[1] not in pinpai:
            pinpai.append(data[1])#获取衣服种类
            xiaoshoui[data[1]]=0


print(pinpai)
print(xiaoshou_0)#
print(xiaoshoui)


for j in range(len(sh)):
    rows = sheet_mo(j).nrows  # 获取多少行
    for xin in range(1, rows):
        data = sheet_mo(j).row_values(xin)
        if data[1] in pinpai:
            xiaoshoui[data[1]]= xiaoshoui[data[1]]+data[4]#获取每个衣服的全年销售量
print(xiaoshoui)

#每种衣服的销售（件数）占比

year_zhanbi = {}
for i in range(len(sh)):
    rows = sheet_mo(i).nrows  # 获取多少行
    for xin in range(1, rows):
        data = sheet_mo(i).row_values(xin)#获取列表
        if data[1] not in year_zhanbi.keys():
            year_zhanbi[data[1]] = 0
for k,l in year_zhanbi.items() :
    zb = l / xiaoshou_0
    year_zhanbi[k] = float(Decimal(zb).quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP))
print(year_zhanbi)

#所有种类衣服字典
# for tt in month_zhanbi.keys():
#     month_zhanbi[tt]=0
# print(month_zhanbi)


month_zhanbi = {}
month_zhanbi_xiaoshou={}
for j in range(len(sh)):
    rows = sheet_mo(j).nrows  # 获取多少行
    month_pinpai = {}
    for aqw in range(len(pinpai)):
        month_xiaohou = 0
        month_pi=0
        for xin in range(1, rows):
            data = sheet_mo(j).row_values(xin)
            if pinpai[aqw] == data[1]:
                month_xiaohou += data[4]
                month_pinpai[data[1]]= month_xiaohou
                for mo,pp in month_pinpai.items():
                    month_pi += pp
                    month_zhanbi
    month_zhanbi_xiaoshou[sh[j]]=month_pinpai
print(month_zhanbi_xiaoshou)



yueyue={}
for i in range(len(sh)):
    yueyue[sh[i]]=0

for k in month_zhanbi_xiaoshou.keys():
    for yueliang in month_zhanbi_xiaoshou[k].values():
        yueyue[k] += yueliang
print(yueyue)
for zl in month_zhanbi_xiaoshou.keys():
    for zbl in month_zhanbi_xiaoshou[zl].keys():
        zbn = month_zhanbi_xiaoshou[zl][zbl] /yueyue[zl]
        zbn = float(Decimal(zbn).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP))
        print(zl, zbl,"月销售占比为",zbn)


print(sal_sum)
ppzs ={}
for i in range(len(sh)):
    rows = sheet_mo(i).nrows  # 获取多少行
    for xin in range(1, rows):
        data = sheet_mo(i).row_values(xin)#获取列表
        if data[1] not in ppzs.keys():
            ppzs[data[1]] = data[2]
            # ppzs[data[1]] = float(Decimal(ppzs[data[1]] / int(sal_sum)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP))

for en in ppzs.keys():
    ad =float(Decimal(ppzs[en]*xiaoshoui[en]/float(sal_sum)).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP))
    print(en,"销售额占比：",ad)
