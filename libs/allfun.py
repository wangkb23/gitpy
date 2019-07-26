#coding=utf-8

import os
import sys
import time
import requests


#reload(sys)
#sys.setdefaultencoding('utf-8')

def alltest():
	return ("abcdef")

def getLog(currentFileName,content):
    ff=open(currentFileName+'.txt','a+')
    ff.write(content)
    ff.close()

#根据uid获取接口验证的字符串
# def getAuth(uid):
#     sttr="java -jar createMauth.jar %s"%(uid)	
#     tmp=os.popen(sttr).read()
#     return tmp[24:89]
#print getAuth(41561)
#查找最新文件
def findf(path):
	redir=path
	lists=os.listdir(redir)
	#print lists
	lists.sort(key=lambda fn:os.path.getmtime(redir+"\\"+fn))
	#文件名
	print (lists[-1])
	ffile=os.path.join(redir,lists[-1])
	#文件路径
	print (ffile)
	return (ffile)

def getTime():
	mstime=float(time.time()*1000)
	mstimes=("%.f" % (float(mstime)))
	mstimestr=mstimes[:-3]
	return mstimestr

def getHeaders():
	#global mstimes,authstrs
	uidstr='10002'#41561 30053946
	mstimes=getTime()
	# authstrs=getAuth(uidstr)
	# headers={"Authorization":"MAuth"+authstrs,
	# "X-APP-ID":"100",
	# "X-Client-ID":"1-100-5beff1fa16b7ef434ac4e46baee420d4-ios",
	# "X-Sign":"32be2ca512905f19de5f53449ef21dc5359b0795",
	# "X-Timestamp":mstimes,
	# "X-WVersion":"3.9.18-0.1.0-d6873feb1ae3598fc2e06fee46db99870d0c962b-iPhone-wxq_AppStore",
	# "ndeviceid":"123456789","X-Matrix-UID":"30003502"}
	# return headers
#print getHeaders()
'''
判断异常参数所有url的返回值，存成一个字典，字典key以序号+:排列，以助于排查不同返回码对应的url
只完成了返回字典，还未完成如何判断每个值并且输出url
'''
def getErrorstat(data4,urls):
	headers=getHeaders()
	errors=['400','404','500','502','503','504']
	errorlt=['','abcdef','~`!@#$%^*()_+?','012345678901']
	dictlt=[]
	for i in data4.keys():
		dictlt.append(i)	
	resdict={}
	k=0
	for i in  dictlt:
		for j in range(len(errorlt)):
			k+=1
			data4[i]=errorlt[j]
			r=requests.get(urls,params=data4,headers=headers)
			rs=r.status_code
			ru=r.url
			resdict[str(k)+':'+str(rs)]=ru	
	for i in resdict.keys():
		if i[2:]=='200':
			print ('返回码200的url： ',resdict[i])
	return resdict

	#print resdict



'''
data4={'communityId':'532712','uid':'41561'}		
url="http://test2.saas.17shihui.com/settlement/trolley/list"
getErrorstat(data4,url)
'''
#print (getTime())