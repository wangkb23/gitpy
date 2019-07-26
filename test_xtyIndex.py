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

class test_xtyIndex(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_xtyIndexMap(self):
        recontent=requests.post(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]
            # print len(dataAll)
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertGreaterEqual(len(dataAll),31,u'信通院首页地图-数据缺失,数据数量为: '+str(len(dataAll))+" "+recontent.url)

  
        
if __name__ == '__main__':
   unittest.main()


