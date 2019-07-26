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

    headers={"Content-Type":"application/json"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"queryType":1,"areaRefeId":3}
    parajs=json.dumps(paramdt)

class test_zxtIndex(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_zxtIndex(self):
        recontent=requests.get(durl)
        rsta=recontent.status_code
        # print type(rsta)
        self.assertEqual(rsta,200,u'知信通首页加载失败,code为: '+str(rsta)+" "+recontent.url)

  
        
if __name__ == '__main__':
   unittest.main()


