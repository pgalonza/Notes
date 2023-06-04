---
title: "PostgreSQL"
draft: false
---

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
