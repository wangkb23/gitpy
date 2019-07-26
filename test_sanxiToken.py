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
    # paramdt={"username":"13520874283","password":"12345678"}
    paramdt={'accountName':(None,'13000000000'),
    'password':(None,'123456'),
    'appId':(None,'IT797f99a8ea461cd06f9735db5033'),
    'loginFrom':(None,'PMS')
    }

class test_sanxiLogin(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_add_url(self):
        recontent=requests.post("http://sanxi.innotree.cn/api/login",files=paramdt,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        print repdt
        self.assertNotIn(rsta,[400,403,500,502],msg=u'服务器,网关错误:'+str(rsta)+recontent.url)
        try:
            compNum=repdt["data"]["accessToken"]
            state=repdt["desc"]
        except Exception, e:
            self.assertEqual (1,0,u"接口未返回结果"+str(rsta))
        # apistatus=repdt["apistatus"]
        if state=="OK":
            self.assertGreaterEqual(len(compNum),10,u'三熙项目登录接口获取token失败:'+str(rsta)+recontent.url)
        else:
            self.assertEqual(1,2,u'三熙项目login接口登录失败:')
        # else:
        #     self.assertEqual(apistatus,1,u'点播视频人数增加接口失败:'+str(rsta)+":"+repdt["errorMsg"]+recontent.url)
         			
        
if __name__ == '__main__':
   unittest.main()


