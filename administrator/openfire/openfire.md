# OpenFire
Memmory
_/etc/sysconfig/openfire_


## DNS
```
SRV recond 1:

service: _xmpp
protocol: _tcp
priority: 0
weigth: 100
port: 5269
hostname: jabber.contora.local.
```
```
SRV recond 2:

service: _xmpp-server
protocol: _tcp
priority: 0
weigth: 100
port: 5269
hostname: jabber.contora.local.
```
```
SRV recond 3:

service: _xmpp-client
protocol: _tcp
priority: 0
weigth: 100
port: 5222
hostname: jabber.contora.local.
```
