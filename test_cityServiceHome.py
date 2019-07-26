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

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36","Content-Type":"application/json;charset=UTF-8"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={}
    parajs=json.dumps(paramdt)

class test_cityServiceHome(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_cityServiceHome(self):
        recontent=requests.get(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]["baseDatas"]
            for i in dataAll.values():
                if i <=1:
                    count+=1
                else:
                    pass
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))

        self.assertLessEqual(count,2,u'区域概览有多项数据小于等于1,数量为: '+str(count)+recontent.url)

        
if __name__ == '__main__':
   unittest.main()


