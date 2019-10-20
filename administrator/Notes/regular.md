# Regular

IP
```
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}'
```

E-mail
```
^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$
```

Url
```
(http|https)://[a-zA-Z0-9./?=_-]*
```

## Mikrotik
Mikrotik social

```
^.+(vk|odnoklassniki|ok|facebook|love.mail|edarling|badoo|topdating|twitter|instagram|ask|meetme).(com|ru|su|ua|net|fm).*$
(^.+|)(smtp\x2Eyandex|pop\x2Eyandex|mail\x2Eyandex|tor-browser|torproject|fishki|facebook|vk|rutube|odnoklassniki|ok|love\x2Email|edarling|badoo|topdating|twitter|instagram|ask|meetme|e\x2Email|mail\x2Erambler|mail\x2Egoogle|mail\x2Eyahoo|cameleo|px2\x2Ezedt|drive\x2Egoogle|cloud\x2Email)\x2E(com|ru|su|ua|net|fm|xyz|eu|org|info|softok).*$
```

## Zabbix
Network interfaces
```
^<?(l2tp|sstp|pptp|ovpn).
```
