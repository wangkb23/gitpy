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
    paramdt={"latestTime":{"code":-1,"min":"2019-07-01","max":"2019-07-31"},"rounds":[],"rankFinancingTime":"false","rankFinancingMoney":"null","rankInvestRounds":"null","rankTotalFinancingMoney":"null","rankRegCapital":"null","pageNum":1,"pageSize":10,"cities":[]}
    parajs=json.dumps(paramdt)

class test_bjjkHjing(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_bjjkHjing(self):
        recontent=requests.post(durl,data=parajs,headers=headers)
        rsta=recontent.status_code
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]        
        try:
            dataAll=repdt["data"]["data"]
            print len(dataAll)
        except Exception, e:
            pass
        self.assertEqual(len(dataAll),10,u'北京金控-华菁数据,数量为: '+str(len(dataAll))+" "+recontent.url)


  
        
if __name__ == '__main__':
   unittest.main()


