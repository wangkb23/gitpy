#coding=utf-8

import sys,os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

reload(sys)
sys.setdefaultencoding('utf8')

fmail=open('./noserep.html','r')
content2=fmail.read()

def email():
    # att1 = MIMEApplication(open('mailtest.txt', 'rb').read())
    # att1.add_header('Content-Disposition', 'attachment', filename='mailtest.txt')
    msg_content = '<html><body><p>当有接口失败时会收到此邮件，请查看详情页结果</p><p><a href="http://172.28.102.148:2500/coreinterface/home">测试报告详情链接</a></p>'+'<p>send by test-wxj ...</p>' +'</body></html>'+content2
    # msg_content = content2
    # msg_content = MIMEText(content2)

    text_html = MIMEText(msg_content,'html', 'utf-8')
    msg = MIMEMultipart()
    # msg.attach(att1)
    msg.attach(text_html)
     
    msg['From'] = formataddr(["管理员",'xinjie.wang@innotree.cn'])     #显示发件人信息
    msg['To'] = formataddr(["相关成员",'xinjie.wang@innotree.cn'])          #显示收件人信息
    # msg['To'] = formataddr(["相关成员",'xinjie.wang@innotree.cn'])          #显示收件人信息
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
# print  content.find("AssertionError")
# print content
if content.find("AssertionError")>0:
	email()
	print u"邮件发送"
else:
	print u"无错误"
#


