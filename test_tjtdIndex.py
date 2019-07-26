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

class test_tjtdIndex(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_tjtdIndex(self):
        recontent=requests.get(durl)
        rsta=recontent.status_code
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]        
        try:
            dataAll=repdt["data"]["baseDatas"]["compNum"]
            print len(dataAll)
        except Exception, e:
            pass
        self.assertEqual(dataAll,538708,u'天津泰达-首页公司数量缺失,数量为: '+str(dataAll)+" "+recontent.url)



  
        
if __name__ == '__main__':
   unittest.main()


