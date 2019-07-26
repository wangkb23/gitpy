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
    # results=getUrlParam.getUP(currentFileName)
    # durl=results[0]
#    paramdt=listToDict.listTD2(results[1][1:]) 
    paramdt={}
    parajs=json.dumps(paramdt)

class test_cityServiceChanye(unittest.TestCase):
    def setUp(self):
        getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
      
    def test_cityServiceComp(self):
        recontent=requests.get("http://api.innotree.cn/uisp/uisp/industryanalysis/companalysis/indextotal?areaId=3&chainId=101000001",data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]
            for i in dataAll.values():
                if i <=1:
                    count+=1
                else:
                    pass
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertLessEqual(count,2,u'产业分析-公司,有多项数据小于等于1,数量为: '+str(count)+recontent.url)

    def test_cityServiceZijin(self):
        recontent=requests.get("http://api.innotree.cn/uisp/uisp/industryanalysis/overview/getrend?chainId=101000001&areaId=3",data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]
            for i in range(len(dataAll)):
                if dataAll[i]["increaseInvestMoney"] <=1:
                    count+=1
                else:
                    pass
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertLessEqual(count,2,u'产业分析-资金链,多项数据小于等于1,数量为: '+str(count)+recontent.url)

    def test_cityServiceJishu(self):
        recontent=requests.get("http://api.innotree.cn/uisp/uisp/industryanalysis/companalysis/industrialchainlink?chainId=101000001&areaId=3&order=4",data=parajs,headers=headers)
        rsta=recontent.status_code
        # print (rsta)
        # print (recontent.content)
        repdt=json.loads(recontent.content)
        # print repdt
        # print repdt["desc"]
        count=0
        try:
            dataAll=repdt["data"]
            for i in range(len(dataAll)):
                if dataAll[i]["patentNum"] <=1:
                    count+=1
                else:
                    pass
        except Exception, e:
            self.assertEqual (1,0,u"Response return status code is "+str(rsta))
        self.assertLessEqual(count,2,u'产业分析-技术链,多项数据小于等于1,数量为: '+str(count)+recontent.url)


        
if __name__ == '__main__':
   unittest.main()


