---
title: "PostgreSQL"
draft: false
description: "PostgreSQL commands and information"
---

{{< toc >}}

What to return for trigger (work with BEFORE)

|trigger invocation|NEW is set|OLD is set|
|------------------|----------|----------|
|ON INSERT         |✔️        |          |
|ON UPDATE         |✔️        |✔️        |
|ON DELETE         |          |✔️        |

Interpretation of privilege symbols

|symbol |description                                          |
|-------|-----------------------------------------------------|
|r      |SELECT ("read")                                      |
|w      |UPDATE ("write")                                     |
|a      |INSERT ("append")                                    |
|d      |DELETE                                               |
|D      |TRUNCATE                                             |
|x      |REFERENCES                                           |
|t      |TRIGGER                                              |
|X      |EXECUTE                                              |
|U      |USAGE                                                |
|C      |CREATE                                               |
|c      |CONNECT                                              |
|T      |TEMPORARY                                            |
|arwdDxt|ALL PRIVILEGES (for tables, varies for other objects)|
|*      |grant option for preceding privilege                 |

Bind to address
_/var/lib/pgsql/data/postgresql.conf_

```text
listen_addresses = 'localhost, ip_address'  
```

_/var/lib/pgsql/data/pg_hba.conf_

```text
host    all             all             0.0.0.0/0          md5
```

Added to SELinux

```text
setsebool -P httpd_can_network_connect_db 1
```

Shared buffers

```text
shared_buffers=<25% of RAM>
```

## Commands

Login as a postgres user

```bash
su - postgres
sudo -u postgres psql
```

Connenct to console

```bash
psql
```

Exit

```bash
\q
```

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

## Queries

Drop tables in schema

```sql
DO $$ DECLARE
rec RECORD;
BEGIN
FOR rec IN (SELECT tablename FROM  pg_tables where schemaname = 'data') LOOP
EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(rec.tablename) || ' CASCADE';
END LOOP;
END;
$$;
```

DROP sequences in schema

```sql
DO $$ DECLARE
rec RECORD;
BEGIN
FOR rec IN (SELECT relname FROM pg_class where relkind = 'S') LOOP
EXECUTE 'DROP SEQUENCE IF EXISTS ' || quote_ident(rec.relname) || ' CASCADE';
END LOOP;
END;
$$;
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

Granting default permissions

```bash
alter default privileges for role <role name> in schema <schema name> grant <statements> on <target object> on <role name>
```

### Role model

Database Owner Role

```sql
CREATE ROLE <database_owner> WITH
NOLOGIN
NOSUPERUSER
NOCREATEDB
NOCREATEROLE
INHERIT
NOREPLICATION
CONNECTION LIMIT -1;
```

Database Creation

```sql
CREATE DATABASE <database_name> WITH
OWNER = <database_owner>
ENCODING = 'UTF8'
TABLESPACE = pg_default
CONNECTION LIMIT = -1
LC_COLLATE = 'en_US.UTF-8'
LC_CTYPE = 'en_US.UTF-8';
```

Objects owner Role

```sql
CREATE ROLE <objects_owner> WITH
NOLOGIN
NOSUPERUSERnew_owner
NOCREATEDB
NOCREATEROLE
INHERIT
NOREPLICATION
CONNECTION LIMIT -1;

GRANT CREATE, CONNECT, TEMPORARY ON DATABASE <database_name> TO <objects_owner> ;
```

Migration User Role

```sql
CREATE ROLE <schema_migration_user> WITH
LOGIN
NOINHERIT
NOSUPERUSER
NOCREATEDB
NOCREATEROLE
NOREPLICATION
CONNECTION LIMIT 10;

GRANT <objects_owner> TO <schema_migration_user>;
ALTER ROLE <schema_migration_user> SET ROLE <objects_owner>;
GRANT CONNECT ON DATABASE <database_name> TO <schema_migration_user>;
```

Security Permissions

```sql
ALTER DEFAULT PRIVILEGES REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;
ALTER ROLE ALL SET search_path = "$user";
REVOKE CONNECTION ON DATABASE <database_name> FROM PUBLIC;
REVOKE USAGE ON SCHEMA public FROM PUBLIC;
```

Application User Role

```sql
CREATE ROLE <service_user> WITH
LOGIN
NOINHERIT
NOSUPERUSER
NOCREATEDB
NOCREATEROLE
NOREPLICATION
CONNECTION LIMIT 10;

GRANT CONNECT, TEMPORARY ON DATABASE <database_name> TO <service_user>;
```

Schema & Access Rights

```sql
CREATE SCHEMA <schema_name> AUTHORIZATION <objects_owner>;
GRANT USAGE ON SCHEMA <schema_name> TO <service_user>;

SET ROLE devops;

ALTER DEFAULT PRIVILEGES FOR ROLE <objects_owner> IN SCHEMA <schema_name>
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO <service_user>;
ALTER DEFAULT PRIVILEGES FOR ROLE <objects_owner> IN SCHEMA <schema_name>
    GRANT SELECT, USAGE ON SEQUENCES TO <service_user>;
ALTER DEFAULT PRIVILEGES FOR ROLE <objects_owner> IN SCHEMA <schema_name>
    GRANT EXECUTE ON FUNCTIONS TO <service_user>;
ALTER DEFAULT PRIVILEGES FOR ROLE <objects_owner> IN SCHEMA <schema_name>
    REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;

RESET ROLE;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA <schema_name
    TO <service_user>;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA <schema_name>
    TO <service_user>;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA <schema_name>
    TO <service_user>;
```

Ownership Assignment

```sql
ALTER DATABASE <database_name> OWNER TO <database_owner>;
ALTER SCHEMA <schema_name> OWNER TO <objects_owner>;
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT table_name FROM information_schema.tables WHERE table_schema = '<schema_name>')
    LOOP
        EXECUTE format('ALTER TABLE <schema_name>.%I OWNER TO <objects_owner>', r.table_name);
    END LOOP;
END
$$;

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT c.relname, n.nspname FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace where c.relkind = 'S' AND n.nspname  = ' <schema_name>')
    LOOP
        EXECUTE format('ALTER SEQUENCE <schema_name>.%I OWNER TO <objects_owner>', r.relname);
    END LOOP;
END
$$;

DO $$
DECLARE
 r RECORD;
BEGIN
 FOR r IN (SELECT viewname FROM pg_views WHERE schemaname = '<schema_name>')
 LOOP
 EXECUTE format('ALTER VIEW <schema_name>.%I OWNER TO <objects_owner', r.viewname);
 END LOOP;
END
$$;

DO $$
DECLARE
 r RECORD;
BEGIN
 FOR r IN (SELECT proname FROM pg_proc WHERE pronamespace = '<schema_name>'::regnamespace)
 LOOP
 EXECUTE format('ALTER FUNCTION <schema_name>.%I OWNER TO new_owner', r.proname);
 END LOOP;
END
$$;
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

## Replication

### Stream

Create replication user

```sql
create role <role name> with replication login password '<password>';
```

Add access in __pg_hba.conf__

```test
host replication <role name> <replica host> md5
```

Change parameters in __postgresql.conf__

```test
wal_level = <logical|replica>
wal_log_hints = on
max_wal_senders = 8
max_wal_size = 1GB
hot_standby = on
```

Restart master

Backup

```bash
pg_basebackup -R -P -X stream -c fast -D <new data dir> -h <master host> -U <role name> -W
```

Check connection string __postgresql.auto.conf__

Start database

## Partitioning

### Horizontal

Create table

```sql
create table <table name> (check (<condition>)) inherits <src table name>;
create index <index name>_idx on <dst table name> (cast(<column name> <column type>));
```

Create rules or triggers

```sql
create or replace rule <rule name> as on insert to <src table name> where <condition> do instead insert into <dst table name> values (new.*);
create or replace rule <rule name> as on update to <src table name> 
where <condition>
do instead insert into <src table name> values (new.*);
    delete from <dst table name> where <condition id>;

create or replace function <function name>_tg() returns trigger as $$
begin
    if <condition> then
        insert into <dst table name> values (new.*);
    else raise exception '<>';
    end if;
    return null;
end;
$$ language plpgsql


create trigger <trigger name> before insert on <src table name>
for each row execute function <function name>_tg(); 
```

Move rows

```sql
with <cte name> as (delete from only <src table name> where <condition> returning *) insert into <dst table name> select * from <cte name>;
```

## Sharding

Create databases

```sql
create database <database name>;
```

Create table on shard with table structure and create index

```sql
create table <table name>(
    <structure>,
    <row name> <row type> check(<condition>),
);

create index <index name>_idx on <table name> (<row name>);
```

Create extension for create remote server

```sql
create extension postgres_fdw;
```

Create server

```sql
create server <server name> foreign data wrapper postgres_fdw options (host '<>', port '<>', dbname '<>');
```

Create user mapping

```sql
create user mapping for <local user name> server <server name> options (user '<remote user name>', password '<>');
```

Create foreign table

```sql
create foreign table <table name> (
<structure>,
)
inherits (<table name>)
server <server name>
options (schema_name '<remote schema name>', table_name '<remote table name>');
```

Function and trigger

```sql
create or replace function <function name>_tg() returns trigger as $$
begin
    if <condition> then
        insert into <dst table name> values (new.*);
    else raise exception '<>';
    end if;
    return null;
end;
$$ language plpgsql


create trigger <trigger name> before insert on <src table name>
for each row execute function <function name>_tg(); 
```

Move rows

```sql
with <cte name> as (delete from only <src table name> where <condition> returning *) insert into <dst table name> select * from <cte name>;
```

##  Row Security Policies(Row Leve Security)

Enable for table

```sql
ALTER TABLE <table name> ENABLE ROW LEVEL SECURITY;
```

Create policy

```sql
CREATE POLICY <policy name> ON <table name> TO <role name> USING (<condition>);
```

Show polices

```sql
SELECT * FROM information_schema.policies;
```

## Connection pooler

- [odyssey](https://github.com/yandex/odyssey)
- [pgbouncer](https://github.com/pgbouncer/pgbouncer)
- [pgpool-II](https://github.com/pgpool/pgpool2)

## Cluster

- [Patroni](https://github.com/patroni/patroni)


Example

- [keycloak-postgresql-ha](https://github.com/pgalonza/keycloak-postgresql-ha)