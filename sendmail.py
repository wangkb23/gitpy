#coding=utf-8

import sys,os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from email.mime.multipart import MIMEMultipart

reload(sys)
sys.setdefaultencoding('utf8')

fmail=open('./noserep.html','rb')
content2=fmail.read()

def email(message):
    #构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    # msg = MIMEMultipart()
    # msg = MIMEText(message, 'plain', 'utf-8')   #message为传入的参数,为发送的消息.
    msg = MIMEText(str(content2), 'utf-8')
    #标准邮件需要三个头部信息： From, To, 和 Subject。
    msg = MIMEMultipart()
    msg.attach(msg)


#     att1 = MIMEText(open('mailtest.txt', 'rb').read(), 'base64', 'utf-8')
#     att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#     att1["Content-Disposition"] = 'attachment; filename="mailtest.txt"'
#     msg.attach(att1)



    msg = MIMEMultipart("mixed")
    msg['From'] = formataddr(["管理员",'xinjie.wang@innotree.cn'])     #显示发件人信息
    msg['To'] = formataddr(["相关成员",'xinjie.wang@innotree.cn'])          #显示收件人信息
    msg['Subject'] = "接口自动化测试报告"      #定义邮件主题
    try:
        #创建SMTP对象
        server = smtplib.SMTP("smtp.mxhichina.com", 80)
        #login()方法用来登录SMTP服务器
        server.login("xinjie.wang@innotree.cn","It6030789000")
        #sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail('xinjie.wang@innotree.cn', ['xinjie.wang@innotree.cn',], msg.as_string())
        print u"邮件发送成功!"
        server.quit()
    except smtplib.SMTPException:
        print u"Error: 系统错误,无法发送邮件"

ff=open('./nosetests.html','r')
content=ff.read()
# print content
if content.find("AssertionError")>0:
	email("api")
	print u"邮件发送"
else:
	print u"无错误"
ff.close()
#


