'''from prettytable import PrettyTable
table=PrettyTable()

print("+-----------------------------------------------------+")
print("|  日期  |  服装名称  |  价格/件  |  库存数量  |  销售量/日  |")
print("  1号   ")
# This is a sample Python script.
'''

print("|               12月份衣服销售数据           |")
print("日期   服装名称   价格/件   库存数量   销售量/每日")
print("1号    羽绒服     253.6    500          10")
print("2号    牛仔裤     86.3     600          60")
print("3号    风衣       96.8     335          43")
print("4号    皮草       135.9    855          63")
print("5号    T恤        65.8     632          63")
print("6号    衬衫       49.3     562          120")
print("7号    牛仔裤     86.3     600           72")
print("8号    羽绒服     253.6    500          69")
print("9号    牛仔裤     86.3     600          35")
print("10号   羽绒服     253.6    500          140")
print("11号   牛仔裤     86.3     600          90")
print("12号    皮草      135.9    855          24")
print("13号    T恤      65.8      632          45")
print("14号    风衣      96.8     335          25")
print("15号    牛仔裤     86.3     600          60")
print("16号    T恤       65.8     632          129")
print("17号    羽绒服     253.6     500         10")
print("18号    风衣       96.8     335          43")
print("19号    T恤       65.8     632          63")
print("20号    牛仔裤    86.3      600          60")
print("21号    皮草      135.9     855          63")
print("22号    风衣      96.8      335          60")
print("23号    T恤       65.8     632           58")
print("24号    牛仔裤    86.3     600           140")
print("25号    T恤      65.8     632            48")
print("26号    风衣      96.8     335           43")
print("27号    皮草      135.9     855          57")
print("28号    羽绒服     253.6    500          10")
print("29号    T恤       65.8     632          63")
print("30号    风衣       96.8     335          78")
num1=(10+69+140+10+10)*253.6+(60+72+35+90+60+60+140)*86.3+(43+25+43+60+43+78)*96.8+(63+24+63+57)*135.9+(63+45+129+63+58+48+63)*65.8+120*49.3
num2=(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)/30
num3=(10+69+140+10+10)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
num4=(60+72+35+90+60+60+140)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
num5=(43+25+43+60+43+78)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
num6=(63+24+63+57)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
num8=(63+45+129+63+58+48+63)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
num9=120/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78)*100
print("经计算，该月的总销售额为：",num1.__round__(2),"元")
print("经计算，该月平均每日销售数量为：",num2.__round__(2),"件")
print("经计算，该月羽绒服、牛仔裤、风衣、皮草、T恤、衬衫各种类月销售量占比分别为：")
print("羽绒服=",num3.__round__(2),"%")
print("牛仔裤=",num4.__round__(2),"%")
print("风衣=",num5.__round__(2),"%")
print("皮草=",num6.__round__(2),"%")
print("衬衫=",num9.__round__(2),"%")
print("T恤=",num8.__round__(2),"%")