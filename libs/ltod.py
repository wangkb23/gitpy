#coding=utf-8

#转化接口参数位字典
def lTod(lt):
	lt2=[]

	for i in range(1,len(lt)):
		lt2.append(lt[i])

	alt=[]
	alt2=[]
	dt={}
	ct=len(lt2)

	for i in range(0,ct,2):
		alt.append(lt2[i])
	for j in range(1,ct,2):
		alt2.append(lt2[j])
	for k in range(len(alt)):
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
