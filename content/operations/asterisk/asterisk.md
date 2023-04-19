---
title: "Asterisk"
draft: false
---

## Links

[Asterisk structure](https://wiki.asterisk.org/wiki/display/AST/Directory+and+File+Structure)

[Asterisk source](https://downloads.asterisk.org/pub/telephony/)

[Jansson source](http://www.digip.org/jansson/releases/)

[pjsip source](https://www.pjsip.org)

## OBDC

_odbc.ini_

```ini
[asteriskcdrdb]
Description=
Driver=MySQL
Server=
Database=
User=
Password=
Port=3306
Socket=/var/lib/mysql/mysql.sock
Option=3
Charset=utf8
```

_cdr_mysql.conf_

```ini
[global]
hostname=
dbname=
table=cdr
password=
user=
port=3306
```

_cdr.conf_

```ini
[general]
enable=yes
unanswered=yes
congestion=yes
safeshutdown=yes
```

_res_odbc.conf_

```ini
[asteriskcdrdb]
enabled=>yes
dsn=>MySQL-asteriskcdrdb
pre-connect=>yes
max_connections=>5
username=>
password=>
database=>asteriskcdrdb
```

_cdr_adaptive_odbc.conf_

```ini
[asteriskcdrdb]
connection=asteriskcdrdb
table=cdr
alias realdst=>realdst
alias remoteip=>remoteip
alias start=>calldate
alias filename=>filename
```
