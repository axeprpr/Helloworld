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
