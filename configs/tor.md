# Tor config files

_torrc_

```
ControlSocket /run/tor/control
ControlSocketsGroupWritable 1
CookieAuthentication 1
CookieAuthFile /run/tor/control.authcookie
CookieAuthFileGroupReadable 1
DataDirectoryGroupReadable 1
CacheDirectoryGroupReadable 1

SOCKSPort 0.0.0.0:9050

ControlPort 9051

HashedControlPassword hash_of_password
CookieAuthentication 1

ORPort 9001
Address 'ip'

Nickname SilvanaRelay1

ContactInfo 0xFFFFFFFF Name <name AT example dot ru>

ExitRelay 0
IPv6Exit 0

IPv6Exit 0

BridgeRelay 1

ExcludeNodes {ru}
```

_torsocks.conf_
```
TorAddress 0.0.0.0
TorPort 9050
OnionAddrRange 127.42.42.0/24
AllowInbound 1
```
