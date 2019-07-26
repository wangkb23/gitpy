#coding=utf-8

import os
import sys
import json
import time
import unittest
import requests
# from libs import allfun
# from libs import getAllid
# from libs import listToDict
# from libs import getUrlParam


#关闭长连接
s = requests.session()
s.keep_alive = False

def getData():
    global durl
    global headers
    global paramdt
    global gcid,giftid
    global reuserid,reliveid


    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}
    #headers=allfun.getHeaders()
    fname = os.path.basename(__file__).split(".")
    currentFileName=fname[0]
    #results=getUrlParam.getUP(currentFileName)
    #durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={"username":"13520874283","password":"12345678"}

class test_innoLogin(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_innoLogin(self):
        recontent=requests.post("https://www.innotree.cn/ajax/uc/login",data=paramdt,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt["msg"]
        try:
            compNum=repdt["data"]["token"]
            state=repdt["msg"]
        except Exception, e:
            self.assertEqual (1,0,u"接口未返回结果"+str(rsta))
        # apistatus=repdt["apistatus"]
        if state==u"成功":
            self.assertGreaterEqual(len(compNum),10,u'官网登录接口获取token失败:'+str(rsta)+recontent.url)
        else:
            self.assertEqual(1,2,u'官网login接口登录失败:'+recontent.url)

        
if __name__ == '__main__':
   unittest.main()


