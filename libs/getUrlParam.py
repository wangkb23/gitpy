#coding=utf-8

import os
import sys
import xlrd
import json
import requests

# reload(sys)
# sys.setdefaultencoding('utf-8')


#fname = os.path.basename(__file__).split(".")
#currentFileName=fname[0]
#print currentFileName
sys.path.append("../../")

def getUP(currentFileName):
	urls=[]
	p={}
	exld=xlrd.open_workbook('.\jkou.xlsx')
	table=exld.sheets()[0]
	#行列表
	rowlt=table.row_values(0)
	#列列表
	collt=table.col_values(1)
	#行数
	ctrow=table.nrows
	#列数
	ctcol=table.ncols
	for i in range(1,ctrow):
		urls.append(table.row_values(i))
		p[table.row_values(i)[0]]=table.row_values(i)[1:]
	#print p
	j=0	
	for i in p.keys():
		if i==currentFileName:
			return p[i][0],p[i]
		else:
			j+=1
			if j==len(p):
				print (u'Excel中没有这个url: %s' % currentFileName)

def getReplaceName():
	pylt=[]
	namelt=[]
	namedt={}
	exld=xlrd.open_workbook('.\jkou.xlsx')
#	worksheet=exld.sheet_by_name('namepy')
	table=exld.sheets()[1]
	#行列表
	rowlt=table.row_values(0)
	#列列表
	collt=table.col_values(1)
	#行数
	ctrow=table.nrows
	#列数
	ctcol=table.ncols
	for i in range(1,ctrow):
		pylt.append(table.row_values(i)[0])
		namelt.append(table.row_values(i)[1])
	for i in range(ctrow-1):
		namedt[pylt[i]]=namelt[i]
	#for k,v in namedt.items():
	#	print k,v
	return pylt,namedt
	
#print getReplaceName()
#print aa[0]
#results=getUP('testxls')
#print results[0]
#print results[1][1:]




