---
title: "PostgreSQL"
draft: false
description: "SQL commands for PostgreSQL"
---

Show parameters

```sql
show <parameter name>;
select current_setting('<parameter name>');
select * from pg_settings where name='<parameter name>'
select * from pg_file_settings where name='<parameter name>;
```

Set parameters in session

```sql
set <parameter name> to '<value>';
select set_config(<parameter name>, <value>,false) 
```

Get path to configuration file

```sql
show config_file;
```

Reload configuration file

```sql
select pg_reload_conf()
```

Show search path

```sql
show search_path;
```

Start vacuum and show progress

```sql
vacuum verbose;
select * from pg_catalog.pg_stat_progress_vacuum;
```

Check shared buffers

```sql
select * from pg_settings where name = 'shared_buffers';
```

Create extension fot view buffers

```sql
CREATE EXTENSION pg_buffercache;
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
```
