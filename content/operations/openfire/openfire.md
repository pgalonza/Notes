---
title: "Openfire"
draft: false
description: "OpenFire notes"
---

{{< toc >}}

Memmory
_/etc/sysconfig/openfire_

## DNS

```text
SRV recond 1:

service: _xmpp
protocol: _tcp
priority: 0
weigth: 100
port: 5269
hostname: jabber.contora.local.
```

```text
SRV recond 2:

service: _xmpp-server
protocol: _tcp
priority: 0
weigth: 100
port: 5269
hostname: jabber.contora.local.
```

```text
SRV recond 3:

service: _xmpp-client
protocol: _tcp
priority: 0
weigth: 100
port: 5222
hostname: jabber.contora.local.
```

## Troubleshooting

UTF-8 encoded messages are saved wrong
_openfire.xml_

```xml
<serverURL>jdbc:mysql://host:3306/openfire?rewriteBatchedStatements=true&amp;useUnicode=true&amp;characterEncoding=UTF-8&amp;characterSetResults=UTF-8&amp;useLegacyDatetimeCode=false&amp;serverTimezone=Europe/Moscow</serverURL>
```
