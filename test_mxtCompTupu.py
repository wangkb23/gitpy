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

    headers={"Content-Type":"application/json","accessToken":"fc8a933e42f8993861820ebf05717c54dead2152530ad93af014bc2c19c6ba4667de96aa56003ddd4d8d42eff7d79254fa7b8a9e42ca613db93c002f959272bb801f17920f33abfd19d1cc37a22cfe9f"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"corpId":16327190365788238362}
    parajs=json.dumps(paramdt)

class test_mxtCompTupu(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_mxtCompTupu(self):
        recontent=requests.get(durl,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]["children"]
            print len(dataAll)
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertGreaterEqual(len(dataAll),2,u'企业图谱-数据返回为空: '+str(len(dataAll))+" "+recontent.url)

  
        
if __name__ == '__main__':
   unittest.main()


