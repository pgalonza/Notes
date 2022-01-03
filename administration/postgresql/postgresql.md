## Postgresql
Bind to address
_/var/lib/pgsql/data/postgresql.conf_
```
listen_addresses = 'localhost, ip_address'  
```

_/var/lib/pgsql/data/pg_hba.conf_
```
host    all             all             0.0.0.0/0          md5
```

Added to SELinux
```
setsebool -P httpd_can_network_connect_db 1
```
