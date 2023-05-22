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
