#!/usr/bin/env python2.6
import sys
import os
import re
import sqlite3
filename = sys.argv[1]
message = open(filename).read()
#message = "".join(message.split())
message = message.replace("\n"," ")
p=re.compile('BEGIN TASK(.*?)END TASK')
m=p.findall(message)

timestemp=os.popen('date +%Y%m%d').read().replace('\n','')
SQLtmp=os.popen('date +%Y%m%d%H%S').read().replace('\n','')+'_axe'+'.sql'
os.environ['SQLtmp']=str(SQLtmp)
os.system('touch $SQLtmp')
for s in m:
    taskname="".join(re.findall(r'^ *(.+?) *\*',s))
    recordsoutput=re.findall(r'Records output.*?\: *(.+?) *Data output',s.replace(',',''))
    elapsedtime="".join(re.findall(r'Elapsed time\: *(.+?) *CPU',s))
    sum=0
    for i in recordsoutput:
        sum+=int(i)
    #print taskname+'|'+str(sum)+'|'+elapsedtime
    sqls="insert into log_check values(\'"+re.sub('[\d\-_]*','',filename)+"\',\'"+taskname+"\',\'"+str(sum)+"\',\'"+elapsedtime+"\',\'"+timestemp+"\');"
    os.environ['sqls']=str(sqls)
    os.system('echo $sqls >> $SQLtmp')

cx = sqlite3.connect("axe.db")
cu = cx.cursor()
cu.execute("create table if not exists log_check(log_name,task_name,output_records_sum,time,batch_id)")
cu.executescript(open(SQLtmp).read())
cx.commit()
cx.close()
os.system('rm -f $SQLtmp')
