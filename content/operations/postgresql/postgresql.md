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
