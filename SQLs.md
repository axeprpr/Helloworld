#####Check PKs of a table(oracle)
```
select a.constraint_name,a.COLUMN_NAME,b.CONSTRAINT_TYPE,b.table_name from user_cons_columns a,
(select CONSTRAINT_NAME,CONSTRAINT_TYPE,table_name from user_constraints where table_name='table_name') b where a.constraint_name=b.CONSTRAINT_NAME;
```
#####Delete a table
```
declare
CURSOR mycursor IS SELECT rowid FROM wow_data.EDM_MS_TEST_OUTPUT_STAGING  WHERE CDE_INSERT_DATE<sysdate-5 ORDER BY rowid;
TYPE rowid_table_type IS TABLE OF rowid index by pls_integer;
v_rowid rowid_table_type;
BEGIN
OPEN mycursor;
LOOP
FETCH mycursor BULK COLLECT INTO v_rowid LIMIT 5000;
EXIT WHEN v_rowid.count=0;
FORALL i IN v_rowid.FIRST..v_rowid.LAST
DELETE wow_data.EDM_MS_TEST_OUTPUT_STAGING WHERE rowid=v_rowid(i);
COMMIT;
END LOOP;
CLOSE mycursor;
END;
/
```
#####LatchFree
```
 select s.SID,
    s.SERIAL#,
    p.SPID,
   s.MACHINE,
    s.OSUSER,
    s.PROGRAM,
    s.USERNAME,
    s.last_call_et,
    a.SQL_ID,
    s.LOGON_TIME,
    a.SQL_TEXT,
    a.SQL_FULLTEXT,
    w.EVENT,
    a.DISK_READS,
    a.BUFFER_GETS
  from v$process p, v$session s, v$sqlarea a, v$session_wait w
 where p.ADDR = s.PADDR
   and s.SQL_ID = a.sql_id
   and s.sid = w.SID
   and s.STATUS = 'ACTIVE'
 order by s.last_call_et desc;
 
 Select sid, p1raw, p2, p3, seconds_in_wait,wait_time, state 
from   v$session_wait 
where  event =’latch free’ 
order by p2, p1raw;
```
##### Check the running session
```
select b.sid oracleID,b.username,b.serial#,spid,paddr,sql_text,b.machine from v$process a, v$session b, v$sqlarea c where a.addr = b.paddr and b.sql_hash_value = c.hash_value;
```
##### Check the locked object
```
select l.session_id sid, s.serial#, l.locked_mode, l.oracle_username, l.os_user_name, s.machine, s.terminal, o.object_name, s.logon_time from v$locked_object l,all_objects o, v$session s WHERE l.object_id = o.object_id and l.session_id = s.sid  order by sid, s.serial#;
```
release this session:
```
ALTER SYSTEM KILL SESSION 'sid,serial#';
```
##### performance: 
```
-- 测定数据的命中率
select metric_name,value from v$sysmetric where metric_name='Buffer Cache Hit Ratio';
-- 查找排序最多的SQL
select * from (select hash_value, sql_text, sorts, executions from v$sqlarea order by sorts desc) where rownum<11;
-- 查找磁盘读写最多的SQL
select * from (select sql_text,disk_reads "total disk", executions "total exec", disk_reads/executions "disk/exec" from v$sql where executions>0 and is_obsolete='N' order by 4 desc) where rownum<11;
-- 查找低效SQL
select executions,disk_reads,buffer_gets,round((buffer_gets-disk_reads)/buffer_gets,2) Hit_radio,round(disk_reads/executions,2) reads_per_run,sql_text from v$sqlarea where executions>0 and buffer_gets >0 and (buffer_gets-disk_reads)/buffer_gets<0.8 order by 4 desc;

-- 查看占io较大的正在运行的session
SELECT se.sid,se.serial#,pr.SPID,se.username,se.status,se.terminal,se.program,se.MODULE,se.sql_address,st.event,st.p1text,si.physical_reads,si.block_changes FROM v$session se,v$session_wait st,v$sess_io si,v$process pr WHERE st.sid=se.sid AND st.sid=si.sid AND se.PADDR=pr.ADDR AND se.sid>6 AND st.wait_time=0 AND st.event NOT LIKE '%SQL%' ORDER BY physical_reads DESC;
```
