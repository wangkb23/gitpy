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
    global paramdt,parajs
    global gcid,giftid
    global reuserid,reliveid


    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36","Content-Type":"application/json"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    results=getUrlParam.getUP(currentFileName)
    durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"template":0,"certificateType":0,"corpName":"","schedulePageNo":-1,"page":1,"size":10}
    parajs=json.dumps(paramdt)
    # print type(paramdt)

class test_mxtJcQuery(unittest.TestCase):
    def setUp(self):
        getData()
      
    def test_mxtJcQuery(self):
    	for i in range(1000):
    		print i
	        recontent=requests.post(durl,data=parajs,headers=headers)
	        rsta=recontent.status_code
	        # print (rsta)
	        # print (recontent.content)
	        repdt=json.loads(recontent.content)
	        # print repdt
	        try:
	            compNum=repdt["data"]["rows"]
	            state=repdt["desc"]
	            print state
	            ccount=repdt["data"]["count"]
	        except Exception, e:
	            self.assertEqual (1,0,e)
	            # self.assertEqual (1,0,u"接口未返回结果，返回码--"+str(rsta))
	        # apistatus=repdt["apistatus"]
	        # if state=="OK":
	        self.assertGreaterEqual(ccount,3,u'贸信通-综合查看-普通认证企业查询结果条数为: '+str(ccount)+" "+recontent.url)
        # else:
        #     self.assertEqual(1,2,u'官网login接口登录失败:'+recontent.url)

        
if __name__ == '__main__':
   unittest.main()


