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
sys.setdefaultencoding('utf8')

def getData():
    global durl
    global headers
    global paramdt
    global parajs


    headers={"Content-Type":"application/json","charset":"utf-8"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"queryWord":"金融"}
    parajs=json.dumps(paramdt)

class test_yanRep(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_add_url(self):
        recontent=requests.post(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        try:
            compNum=repdt["data"]["count"]
        except Exception, e:
            self.assertEqual (1,0,u"接口未返回结果"+str(rsta))
        # apistatus=repdt["apistatus"]
        self.assertGreaterEqual(int(compNum),100000,u'BI(I)研报搜索关键字金融-研报数量少于预期值10w,(before 108624),本次结果为: '+str(compNum)+" "+recontent.url)
        # if rsta==200:
        #     pass
        # else:
        #     self.assertEqual(1,2,u'三熙首页加载失败,返回码 '+str(rsta) +recontent.url)

        
if __name__ == '__main__':
   unittest.main()


