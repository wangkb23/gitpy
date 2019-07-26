#coding=utf-8
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def findf(path):
	redir=path
	lists=os.listdir(redir)
	#print lists

	lists.sort(key=lambda fn:os.path.getmtime(redir+"\\"+fn))
	#文件名
	print lists[-1]
	ffile=os.path.join(redir,lists[-1])
	#文件路径
	print ffile
	return ffile

findf('../')