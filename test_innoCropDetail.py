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
    # headers={"Content-Type":"application/json","charset":"utf-8",}
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}
    durl=results[0]
    # paramdt=listToDict.listTD2(results[1][1:])
    # paramdt={"username":"13520874283","password":"12345678"}
    paramdt={}
    # parajs=json.dumps(paramdt)

class test_innoCropDetail(unittest.TestCase):
    def setUp(self):
    	getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
	
    def test_corpNum(self):
        recontent=requests.get(durl,data=paramdt,headers=headers)
        rsta=recontent.status_code
        #print recontent.url
        # print (recontent.content)
        self.assertNotIn(rsta,[400,401,403,500,502],msg=u'服务器,网关错误:'+str(rsta)+recontent.url)
        repdt=json.loads(recontent.content)            
        # print repdt
        #公司结果数
        try:
            compNum=repdt["data"][0]["introduction"]
        except Exception, e:
            self.assertEqual (1,0,u"接口未返回结果")
        self.assertGreaterEqual(len(compNum),600,u'官网公司详情页内容介绍长度少于预期值600(before 751),本次结果为: '+str(len(compNum))+" "+recontent.url)
        # self.assertGreaterEqual(len(restr),1,paramdt["areaName"]+" 省区域内容为空: "+recontent.url)
        # cityName=repdt["data"]["provinceNewTechCompanyNums"][0]["areaName"]
        # self.assertEqual(parName,cityName,"入参-"+parName+" Json-"+cityName+" False")
        # self.assertGreaterEqual(len(cityNum),1,paramdt["areaName"]+" 八项指标内容为空: "+recontent.url)


if __name__ == '__main__':
    # path= os.path.dirname(__file__)
    # outfile = os.path.join(path, 'test_searchCorpTag.py')
    # run(argv=['nosetests', '-v','--with-html-output','--html-out-file=result.html',outfile],plugins=[HtmlOutput()])

    # #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    unittest.main()









