---
title: "Amavis"
draft: false
description: "Amavis notes"
---

{{< toc >}}

## Tuning

_/etc/amavis/amavisd.conf_

```text
$max_servers = 10;
```

_/etc/postfix/master.cf_

```text
smtp-amavis unix -       -       n      -     10 smtp
```

## Tools

Clean database

```sql
DELETE FROM msgs WHERE quar_type = 'Q' AND time_num < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 20 DAY));
DELETE msgrcpt.* FROM msgrcpt INNER JOIN msgs ON msgrcpt.mail_id=msgs.mail_id WHERE msgs.time_num < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 20 DAY));
DELETE FROM msgs WHERE time_num < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 20 DAY));
DELETE FROM msgrcpt WHERE NOT EXISTS (SELECT 1 FROM msgs WHERE mail_id=msgrcpt.mail_id);
DELETE FROM quarantine WHERE NOT EXISTS (SELECT 1 FROM msgs WHERE mail_id=quarantine.mail_id);
DELETE FROM maddr WHERE NOT EXISTS (SELECT 1 FROM msgs WHERE sid=id) AND NOT EXISTS (SELECT 1 FROM msgrcpt WHERE rid=id);
DELETE FROM mailaddr WHERE NOT EXISTS (SELECT 1 FROM wblist WHERE sid=id);
```
