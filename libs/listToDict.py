#coding=utf-8


'''
解决从excel中读取列表转化为字典的问题，使之成为参数字典格式
'''
def listTD2(lt):
	lt2=[]
	lt3=[]
	dt={}
	count=len(lt)
	if count%2==1:
		lt.append('')
		lt2=lt
	elif count%2==0:
		lt2=lt
#	print lt2
	for j in range(len(lt2)):
		lt3.append(str(lt2[j])) #str解决取出的数字带小数点的问题
	for k in range(0,len(lt2),2):
		dt[lt3[k]]=str(lt3[k+1])
	return dt

	'''	
	for i in range(count):
		if lt[i]=='':
			num=i+1
			break;	
	'''


#a=['1','2','3','4','5','6','7']
#print listTD2(a)
#转化接口参数位字典
def listTD(lt):
	lt2=[]

	for i in range(1,len(lt)-1):
		lt2.append(lt[i])

	alt=[]
	alt2=[]
	dt={}
	ct=len(lt2)

	for i in range(0,ct,2):
		alt.append(lt2[i])
	for j in range(1,ct,2):
		alt2.append(lt2[j])
	for k in range(len(alt)-1):
		dt[alt[k]]=alt2[k]
	return dt


'''
ab={1:['wwww.baidu.com',1,2,3,4]}
ltab=ab[1]
ltab2=[]
for i in range(1,len(ltab)):
	ltab2.append(ltab[i])
print ltab2
'''

def zhi(lt):
	k=[]
	for i in lt:
		for j in i.split(','):
			k.append(j)
	return k

#print zhi(a)