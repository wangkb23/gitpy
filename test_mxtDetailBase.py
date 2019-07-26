#coding=utf-8

import os
import sys
import json
import time
import unittest
import requests
from libs import allfun
from libs import getAllid
from libs import listToDict
from libs import getUrlParam


#关闭长连接
s = requests.session()
s.keep_alive = False

reload(sys)
sys.setdefaultencoding('utf-8')

tt=requests.get("http://172.28.102.148:2500/innotreetest/gettoken").content
print tt


def getData():
    global durl
    global headers
    global paramdt,parajs

    headers={"Content-Type":"application/json","accessToken":tt}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"corpId":16327190365788238362}
    parajs=json.dumps(paramdt)

class test_mxtDetailBase(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_mxtDetailBase(self):
        recontent=requests.get(durl,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            cmpName=repdt["data"]['corpName']
            cmpCapital=repdt["data"]['capital']
            cmpAdd=repdt["data"]['address']
            # print cmpName
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertNotEqual(cmpName,'',msg=u"公司名称为空 "+recontent.url)
        self.assertNotEqual(cmpCapital,'',msg=u"注册资本为空 "+recontent.url)
        self.assertNotEqual(cmpAdd,'',msg=u"公司地址为空 "+recontent.url)

    def test_mxtDetailTupu(self):
        recontent=requests.get("http://www.trustrader.cn/api/paas/corp/detail/relations?corpId=16327190365788238362",headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            cmpNum=repdt["data"]['children']
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertGreaterEqual(cmpNum,1,msg=u"企业图谱为空 "+recontent.url)


        
if __name__ == '__main__':
   unittest.main()


