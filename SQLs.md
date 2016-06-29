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
