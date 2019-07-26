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

class test_huajBgouLy(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_huajBgouLy(self):
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
            print len(dataAll)
        except Exception, e:
            pass
        self.assertGreaterEqual(len(dataAll),9,u'华菁并购-按并购方领域搜索,数据缺失,领域为金融APP,领域标签长度为: '+str(len(dataAll))+" "+recontent.url)
        
if __name__ == '__main__':
   unittest.main()


