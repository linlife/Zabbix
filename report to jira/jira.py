#!/usr/bin/env python
#coding:utf-8
import os
import sys


subject=sys.argv[2]
content=sys.argv[3].strip()

	
#data={"fields": {"project":{ "key": "ZABBIX" }, "summary": "%s"%subject, "description": "book",  "issuetype": { "name": "Bug"}}}

os.system("wget --post-data=\'{\"fields\": {\"project\":{ \"key\": \"ZABBIX\" }, \"summary\": \"%s\", \"description\": \"%s\",  \"issuetype\": { \"name\": \"Bug\"}}}\' --no-check-certificate --header=\"Authorization: Basic emFiYml4X21vbml0b3I6VGVtcDEyMyFAIw==\" --header=\"Content-Type: application/json\" https://10.10.10.36/rest/api/2/issue/ --delete-after"%(subject,content))


