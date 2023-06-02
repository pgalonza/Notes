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
