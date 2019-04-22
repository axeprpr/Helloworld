#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import urllib,urllib2,json,sys,random,os,platform
import ConfigParser
from prettytable import PrettyTable

reload(sys)
sys.setdefaultencoding('utf8')

# get frpc configuration
req = urllib2.Request("http://astute-tec.com:20003/api/proxy/tcp", headers={"Authorization": "Basic YWRtaW46YWRtaW4="})
response = urllib2.urlopen(req)
tcp = response.read()

x = PrettyTable(["Name", "Port", "Status"])
for i in json.loads(tcp).get('proxies', []):
    try:
        x.add_row([i.get('name') ,i.get('conf').get('remote_port'), i.get('status')])
    except:
        pass

print(x)
if 'windows' in platform.system().lower():
    os.system('pause')
