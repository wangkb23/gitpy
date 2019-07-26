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

def getData():
    global durl
    global paramdt,paramdt2
    global headers
    global parajs
    
#     fname = os.path.basename(__file__).split(".")
#     currentFileName=fname[0]
#     results=getUrlParam.getUP(currentFileName)
# #    print results[1][1:]
#     #headers=allfun.getHeaders()
#     headers={"Content-Type":"application/json","charset":"utf-8",}
#     durl=results[0]
#     paramdt=listToDict.listTD2(results[1][1:])
#     paramdt["tags"]=["金融"]
#     parajs=json.dumps(paramdt)

class test_tagCorp(unittest.TestCase):
    def setUp(self):
    	getData()

#    def test_error_url(self):
#        dt=allfun.getErrorstat(paramdt,durl)
#        print dt
	
    def test_corpNum(self):
        # recontent=requests.post(durl,data=parajs,headers=headers)
        # rsta=recontent.status_code
        #print recontent.url
        # print (recontent.content)
        dt={}
        for i in range(5):
            print i
            if i>=2:
                try:
                    self.assertEqual(1,0,str(i)+" is wrong")
                except Exception, e:
                    dt[i]="wrong"
                    print str(i)+" is wrong"
            else:
                dt[i]="right"
        # print dt

        for j in dt.keys():
            if dt[j]=="wrong":
                self.assertEqual(1,0,str(j)+"is wrong")
            else:
                print "right"


        # self.assertNotIn(rsta,[401,403,500,502],msg=u'服务器,网关错误:'+str(rsta)+recontent.url)
        # repdt=json.loads(recontent.content)            
        # #公司结果数
        # try:
        #     compNum=repdt["data"]["total"]
        # except Exception, e:
        #     self.assertEqual (1,0,u"接口未返回结果")
        # self.assertGreaterEqual(int(compNum),110000,u'金融tag公司数量少于11w: '+str(compNum))


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









