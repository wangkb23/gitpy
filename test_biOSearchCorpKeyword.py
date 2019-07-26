#coding=utf-8

import os
import sys
import json,urllib
import requests
import unittest
from libs import allfun
from libs import listToDict
from libs import getUrlParam
from libs import getAllid

reload(sys)
sys.setdefaultencoding('utf8')
#关闭长连接
s = requests.session()
s.keep_alive = False

def getData():
    global durl
    global paramdt,paramdt2
    global headers
    global parajs
    
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
#    print results[1][1:]
    #headers=allfun.getHeaders()
    headers={"Content-Type":"application/json","charset":"utf-8",}
    durl=results[0]
    # paramdt=listToDict.listTD2(results[1][1:])
    # paramdt["tags"]=["金融"]
    paramdt={"matches":{  }}
    parajs=json.dumps(paramdt)

class test_biOKeyCorp(unittest.TestCase):
    def setUp(self):
    	getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
	
    def test_corpNum(self):
        recontent=requests.post(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        #print recontent.url
        # print (recontent.content)
        self.assertNotIn(rsta,[401,403,500,502],msg=u'服务器,网关错误:'+str(rsta)+recontent.url)
        repdt=json.loads(recontent.content)        
        #公司结果数
        try:
            compNum=repdt["data"]["count"]
        except Exception, e:
            self.assertEqual (1,0,u"接口未返回结果")
        self.assertGreaterEqual(int(compNum),4000000,u'BI(O)公司搜索关键字金融-公司数量少于预期值4w,本次结果为: '+str(compNum)+" "+recontent.url)

if __name__ == '__main__':
    unittest.main()









