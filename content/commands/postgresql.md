---
title: "PostgreSQL"
draft: false
description: "SQL commands for PostgreSQL"
---

Set parameters in session

```sql
set <parameter name> to '<value>';
select set_config(<parameter name>, <value>,false) 
```

Reload configuration file

```sql
select pg_reload_conf()
```

Start vacuum and show progress

```sql
vacuum verbose;
select * from pg_catalog.pg_stat_progress_vacuum;
```

Quotes

```sql
quote_ident() -- ""
quote_literal() -- ''
```

Start database

```bash
pg_ctl -D <data dir> start
postgres -D <data dir>
```

Promote replica

```bash
pg_ctl promote -D <data dir>
```

Move row in other table

```sql
with <cte name> as (delete from <only> <src table> where <condition> returning *) insert into <dst table> select * from <cte name>;
```

## Show informations

Show parameters

```sql
show <parameter name>;
select current_setting('<parameter name>');
select * from pg_settings where name='<parameter name>'
select * from pg_file_settings where name='<parameter name>;
```

Show database size

```sql
select pg_size_pretty(pg_database_size(current_database()));
```

Show table size

```sql
SELECT pg_size_pretty(pg_relation_size('<table name>'));
SELECT relname, relpages FROM pg_class ORDER BY relpages DESC;
```

Get path to configuration file

```sql
show config_file;
```

Check shared buffers

```sql
select * from pg_settings where name = 'shared_buffers';
```

Show search path

```sql
show search_path;
```

Show WAL`s

```sql
select * from pg_ls_waldir();
```

Show LSN

```sql
SELECT pg_current_wal_lsn();
```

Show locks

```sql
select * from pg_locks;
select pg_blocking_pids(<pid>);
```

Show current pid

```sql
select pg_backend_pid();
```

Get stats

```sql
select * from pg_stat_database;
select * from pg_class;
select * from pg_stats;
select * from pg_stat_activity;
select * from pg_stat_user_tables;
select * from pg_stat_user_indexes;
select * from pg_stat_statements;
select * from pg_catalog.pg_stat_replication;
```

Show databases and tables

```sql
SELECT datname FROM pg_database
WHERE datistemplate = false;

SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;
```

## Privileges

Show table privileges

```bash
\dp+ *.*
```

Show default table privileges

```bash
\ddp+ *.*
```

Show schema privileges

```bash
\dn+
```

Show database privileges

```bash
\l
```

Show roles privileges

```bash
\duS+
```

Show roles

```sql
select * from pg_catalog.pg_shadow;
```

Granting the permissions to transfer privileges

```sql
GRANT <statements> ON <table name> TO <role name> WITH GRANT OPTION;
GRANT <statements> ON <role name>.<table name> TO <role name>;
```

## Functions

Show functions

```sql
select * from information_schema.routines where routine_type = 'FUNCTION' and routine_schema = '<schema name>';
```

Return value

```sql
create or replace function <function name>(<variable name> <variable type>, out <variable name> <variable type>) as $$
begin
    <query>
end;
$$ language plpgsql

create or replace function <function name>(<variable name> <variable type>) returns <variable type> $$
declare <variable name> <variable type>;
begin
    <query>
    return <variable name>;
end;
$$ language plpgsql
```

Loop

```sql
create or replace function <function name>(variable name> <variable type>) returns table (<variable name> <variable type>, <variable name> <variable type>) as $$
declare <variable name> <variable type>;
begin
    <query>
    into <variable name>;
end;
$$ language plpgsql

create or replace function <function name>(<variable name> <variable type>, out <variable name> <variable type>, out <variable name> <variable type>) returns setof record as $$
begin
    <query>
    into <variable name>;
end;
$$ language plpgsql
```

Return table from query

```sql
create or replace function <function name>(<variable name> <variable type) 
    returns setof <table name> as $$
begin
    return query
    <query>;
end;
$$ language plpgsql

create or replace function <function name>(<variable name> <variable type) 
    returns <setof> <table name> as $$
    <query>;
$$ language sql

create or replace function <function name>(<variable name> <variable type, out <variable name> <variable type>) 
    returns setof record as $$
    <query>;
$$ language sql
```

Anonymous function

```sql
do $$
declare
    <variable name> = <query>;
begin
    execute '<query>' || <variable name>;
end;
$$ language plpgsql
```

## PL/Python

```sql
create or replace function <function name>(<variable name> <variable type, out <variable type>) as $$
    <variable name> = plpy.execute('<query>')
    return <variable name>[<list index>][<dict key>]
$$ language plpython3u;

create or replace function <function name>(<variable name> <variable type) returns <variable type> as $$
    <variable name> = plpy.execute('<query>')
    return <variable name>[<list index>][<dict key>]
$$ language plpython3u;
```

## Trigger

Show triggers

```sql
select * from information_schema.triggers;
select * from pg_event_trigger;
```

Data changes

```sql
create or replace function <function name>_tg() returns trigger as $$
begin
    new.<row name> = <query>;
    ---
    <insert|update|delete query>;
    return <null|new|old>;
end;
$$ language plpgsql


create trigger <trigger name> <before|after|instead of> 
<update|insert|delete|truncate> on <table name>
for each <row|statement> when (<condition>) execute <procedure|function> <function name>_tg(); 
```

Database event

```sql
create or replace function <function name>_tg() returns event_trigger as $$
begin
    for i in select * from pg_event_trigger_ddl_commands()
    loop
        <query>;
    end loop;
end;
$$ language plpgsql

create event <trigger name> on <ddl_command_start,ddl_command_end|sql_drop|table_rewrite> execute function <function name>_tg();
```

## Procedure

Show functions

```sql
select * from information_schema.routines where routine_type = 'PROCEDURE' and routine_schema = '<schema name>';
```

```sql
create or replace procedure <procedure name>() as $$
begin
    <query>;
    commit;
end;
$$ language plpgsql;

call <procedure name>();
```

## Views

Show views

```sql
select * from information_schema.views;
```

Create view

```sql
create view <view name> as
    <query>;

select * from <view name>;
```

## Extensions

Show extensions

```sql
select * from pg_catalog.pg_available_extensions;
```

Create extension for view buffers

```sql
CREATE EXTENSION pg_buffercache;
```

## Rules

Create rule

```sql
create or replace rule <rule name> as on <insert|update|delete> to <src table name> where <condition> do instead <insert|update|delete> into <dst table name>; -- <values (new.*)> for insert
```

Show rules

```sql;
select * from pg_rules;
```

## Table

Create table with same structure

```sql
create table <to table name> as table <from table name> with no data;
```

Create inherits

```sql
create table <table name> (check (<condition>)) inherits <src table name>;

create index <index name>_idx on <dst table name> (cast(<column name> <column type>));
```

Create temp table

```sql
create temporary table <table name>_temp as (select * from <table name>);
```
