#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import urllib2
import urllib
import simplejson
import sys
import time

corpid='*******************************'
corpsecret='m-*******************************'
get_token='***********************************'%(corpid,corpsecret)
#time.sleep(5)
content=sys.argv[3]

f=open('/etc/zabbix/alertscripts/contfile','w')
f.write('%s'%content)
f.close

toparty=sys.argv[1]
data={
    "toparty":"%s"%toparty,
#    "toparty":"1",
    "msgtype":"text",
    "agentid":"1",
    "text":{"content":"%s"%content},
    "safe":"0",
}

data=simplejson.dumps(data,ensure_ascii=False)
#data=simplejson.dumps(data)

f=urllib2.urlopen(get_token)
s=f.read()
f.close()
token=s.split('"')[3]

msm_post='**********************************'%token
f=urllib2.urlopen(msm_post,data)
content =f.read()
f.close()


