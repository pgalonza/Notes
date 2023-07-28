---
title: "Email"
draft: false
---

{{< toc >}}

## POSTFIX

Check configuration

```bash
postfix check
postconf
```

Queue view

```bash
mailq | less
postqueue -p | less
mailq | grep Request
find /var/spool/postfix/deferred -type f | wc -l
find /var/spool/postfix/active -type f | wc -l
find /var/spool/postfix/incoming -type f | wc –l
```

Queue send

```bash
postqueue -f
mailq -q
postsuper -r ALL
postqueue -i <ID-mail>
postsuper -r <ID-mail>
postqueue -s <domain>
```

Queue drop

```bash
postsuper -d ALL
postsuper -d deferred
postsuper -d <ID-mail>
```

Queue halt

```bash
postsuper -h <ID-mail>
postsuper -h ALL
postsuper -h deferred
```

Queue run

```bash
postsuper -H <ID-mail>
postsuper -H ALL
```

## Mail

Mail console client

```bash
mutt -f
```

Send mail

```bash
(echo  "Subject: test1"; echo "test2";)|sendmail -f sender@domain.com recipient@domain.com
```

## Dovecot

Quota

```bash
dovecot set quota
```

Reload the dovecot

```bash
doveadm reload
```

Show who connected

```bash
doveadm who -1
```

Clean the authorization cache

```bash
doveadm auth cache flush
```
