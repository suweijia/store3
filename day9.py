import xlrd
import pymysql
# 打开工作簿
con = pymysql.connect(host="localhost",user="root",password="",database="xiaoshou")
sl = xlrd.open_workbook(filename=r"E:\狼腾\python自动化\day07\任务\2020年每个月的销售情况.xls",encoding_override=True)

sh = list(sl.sheet_names())
#data = sh[1].cell_value(0,1)定位单元格   print(data)
#获取某个sheet文件内容
# def sheet_mo(month):
#     shm= sl.sheet_by_name(sh[month])
#     return shm

cur = con.cursor()#游标

for sht in sh:
    wb = sl.sheet_by_name(sht)
    sql ="create table {}(日期 VARCHAR(5),服装名称 VARCHAR(5),价格 DOUBLE(10,1),本月库存量 Int(10),销售量 Int(10))"
    cur.execute(sql.format(sht))
    row_num = wb.nrows
    con.commit()
    for i in range(1,row_num):
        row_data= tuple(wb.row_values(i))
        sql1="insert into {} value{}"
        cur.execute(sql1.format(sht,row_data))
        con.commit()
cur.close()
con.close()
