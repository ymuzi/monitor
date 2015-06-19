# encoding: utf-8
import os,sys,string
import urllib2
import json
import codecs

#test1 test1source.txt
test = 0

try:
    if test != 1:
        s = urllib2.urlopen("http://store.ccb.com//mcmsfe/queryAppList.gsp?osType=IOS").read()
        srcStr = s.decode('gbk').encode('utf-8')
        print '----------------------------'
        print u'begain....'
    else:
        if(os.path.exists("./source.txt")):
            srcfile = open("./source.txt",'r')
            srcStr = srcfile.read()
            srcfile.close()
        else:
            print u"soure.txt is missing"
        print '----------------------------'
        print u'test is begain...'
        
    jsObj = json.loads(srcStr)
    #print jsObj
    
    template = open("./template.plist",'r')
    tlStr = template.read();
    template.close()
    
    apps = jsObj['apps']
    for app in apps:
        appId = app['appId']
        appPkg = app['appPkg']
        appVersion = app['appVersion']
        appName = app['appName']
        
        fileName = './'+appId+'.plist'
        if(os.path.exists(fileName)):
            os.remove(fileName) 
            
        content = tlStr%(appId,appId,appPkg,appVersion,appName,appName)
        print 'content:'+content
        dest = codecs.open(fileName,'w',"utf-8")
        dest.write(content);
        dest.close()
    print 'complete'
    print '-------------------------'
except urllib2.HTTPError,e:
   print e.code