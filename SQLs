#####Check PKs of a table(oracle)
```
select a.constraint_name,a.COLUMN_NAME,b.CONSTRAINT_TYPE,b.table_name from user_cons_columns a,
(select CONSTRAINT_NAME,CONSTRAINT_TYPE,table_name from user_constraints where table_name='MS_EDM_EVENTS_REF_DLTA ') b where a.constraint_name=b.CONSTRAINT_NAME;
```
