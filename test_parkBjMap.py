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


def getData():
    global durl
    global headers
    global paramdt,parajs

    headers={"Content-Type":"application/x-www-form-urlencoded"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"provinceId":"110100"}
    parajs=json.dumps(paramdt)

class test_parkBjMap(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_parkBjMap(self):
        recontent=requests.post(durl,data=paramdt,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        sum=0
        try:
            dataAll=repdt["data"]["data"]
            # print dataAll
            # print len(dataAll)
            for i in range(len(dataAll)):
                # print i
                sum=sum+dataAll[i]["parkNum"]
                # print dataAll[i]["parkNum"]
            # print sum
        except Exception, e:
            pass
        self.assertGreaterEqual(sum,300,u'数字园区_北京园区总数缺失，数量为 '+str(sum)+" "+recontent.url)
        
if __name__ == '__main__':
   unittest.main()


