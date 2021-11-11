fopen=open(file="E:\\狼腾\\python自动化\\day15【异常处理和文件读写】\\任务\\baidu_x_system.log",mode="r+",encoding="utf-8")
tn = fopen.readlines()
tp={}
try:
    for i in tn:
        httpsl=i[0:i.rfind(' - - ',+1)]#读取' - - '之前的字符串
        if httpsl not in tp.keys():
            tp[httpsl]=1
        else:
            tp[httpsl]+=1
    for vl in tp:
        print("{}出现的次数为：{}".format(vl,tp[vl]))
except Exception:
    print("加载不出来")
finally:
    print("ok")


