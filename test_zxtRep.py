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
# print tt

def getData():
    global durl
    global headers
    global paramdt,parajs

    headers={"Content-Type":"application/json","accesstoken":tt}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"corpId":"7846709520752062541"}
    parajs=json.dumps(paramdt)

class test_zxtRep(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_zxtRep(self):
        recontent=requests.post(durl,data=paramdt,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        try:
            dataAll=repdt["data"]
            # print dataAll
            # print len(dataAll)
        except Exception, e:
            pass
        self.assertGreaterEqual(len(dataAll),13,u'知信通_评估报告，数据缺失,公司因果树，报告列表长度为: '+str(len(dataAll))+" "+recontent.url)


if __name__ == '__main__':
   unittest.main()


