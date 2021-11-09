import smtplib
from email.mime.text import MIMEText      #mimrtext()定义邮件正文
from email.mime.multipart import MIMEMultipart #mimemulipart模块构造带附件

def sendemailwithfile():
    #发送邮件的服务器
    smtpserver = 'smtp.qq.com'
    #发送邮件用户和密码
    user ='599789637@qq.com'
    password = 'hxcmgzgcvpuvbfdi'
    #发送者
    sender = '599789637@qq.com'
    #接收者
    receiver = '2431320433@qq.com'
    #邮件主题
    subject = "苏维嘉"
    #发送附件
    sendfile = open("D:\\python\\pythonProject\\自动化\day13\\计算器.html","rb").read()
    att = MIMEText(sendfile,"base64","utf-8")
    att["content-type"] = "application/octet-stream"
    # att["content-disposition"] = "attachment;filename = '计算器.html'"
    att.add_header('Content-Disposition', 'attachment', filename='计算器.html')
    msgroot = MIMEMultipart('related')
    msgroot['subject'] = subject
    msgroot.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msgroot.as_string())
    smtp.quit()
sendemailwithfile()
