#coding=utf-8
import re
import sys,os,datetime
from libs import getUrlParam

now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

reload(sys)
sys.setdefaultencoding('utf8')

ff=open('./nosetests.html','r')
content=ff.read()

lt,dt=getUrlParam.getReplaceName()

for i in lt:
	for j in dt.keys():
		if i==j:
			# print (dt[i])fghjkl;''
			content=content.replace(str(i),dt[i])
content=content.replace("Test case","Test case "+str(now_time))
content=content.replace("<th>Total</th>","<th>Total</th><p align='center'> <font size='5'><a href='http://172.28.102.148:2500/innotreetest/home'>返回主页</a></font> </p>")

ff2=open("./noserep.html",'w')
ff2.write(content)
ff2.close
ff.close



'''
redir='F:\\interface'
lists=os.listdir(redir)
#print lists
#查询最新文件
lists.sort(key=lambda fn:os.path.getmtime(redir+"\\"+fn))
print lists[-1]
ffile=os.path.join(redir,lists[-1])
print ffile

'''


