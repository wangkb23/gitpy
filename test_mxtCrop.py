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
    paramdt={"source":"TRUSTRAER","type":2,"andOr":1,"page":1,"pageSize":10,"keywords":"","tags":[],"operation":{"status":""},"reg":{"capital":{"code":"","max":"","min":""},"regTime":{"code":"","max":"","min":""},"area":{"province":"","city":"","district":""}},"advanced":{"patent":""},"trustFilter":{"corpTrustType":"","latestTradeDate":"","majorExportRegion":"","currency":""},"direction":1}
    parajs=json.dumps(paramdt)

class test_mxtCrop(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_mxtCrop(self):
        recontent=requests.post(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        try:
            compNum=repdt["data"]["total"]
            print compNum
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))

        self.assertGreaterEqual(compNum,29766098,u'查询结果少了300万,之前结果为32766098,现在为: '+str(compNum)+recontent.url)

        
if __name__ == '__main__':
   unittest.main()


