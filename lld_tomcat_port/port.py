#!/usr/bin/env python
#encoding:utf-8
import os
import simplejson

def dirfind(mypath):
    dirlist=mypath.split('/')
    if dirlist[-1]=='conf':
        return dirlist[-2]
    else:
        return None


def portfind(fullpath,filename):
    a=os.popen('grep http.port %s/%s | awk -F\'=\' \'{print $2}\''%(fullpath,filename)).read().strip()
    if a !='':
        b=os.popen("netstat -tnlp | grep \'\\b%s\'"%a).read().strip()
        if b!='':
            return a
        else:
            return None
    else:
        return None


def tomcat_discovery():
    lst=[]
    for root,dir,files in os.walk("/opt/app/tomcat"):
        for file in files:
            if file=='catalina.properties' :
                dname=dirfind(root) 
                dport=portfind(root,file)
#                print dport
                if dname != None and dport != None:
                    lst +=[{'{#DIRNAME}':dname,'{#HTTPPORT}':dport}]
    print simplejson.dumps({'data':lst},ensure_ascii=False)
                

if __name__=='__main__':
    tomcat_discovery()
