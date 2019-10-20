# Amavis
## Tuning
_/etc/amavis/amavisd.conf_
```
$max_servers = 10;
```

_/etc/postfix/master.cf_
```
smtp-amavis unix -       -       n      -     10 smtp
```
