#!/usr/bin/env python
import os
import sys
import simplejson

def disk_discovery():
    f=os.popen("sar -d 1 1 | grep Average | grep -v DEV | awk -F' '  '{print $2}'")
    disklist=f.read().strip().split('\n')
    f.close()
    
#    print '{'
#    print '\t"data":['
#    for i in disklist:
#        print '\t\t{\"{#diskname}\":\"%s\"}'%i 
#    print '\t]'
#    print '}'
    lst=[]
    for i in disklist:
        lst +=[{'{#DISKNAME}':i}] 
    print simplejson.dumps({'data':lst},ensure_ascii=False)



if __name__ == '__main__':
    disk_discovery()
