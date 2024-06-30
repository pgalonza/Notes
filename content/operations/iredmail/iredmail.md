---
title: "iRedMail"
draft: false
description: "IredMail notes"
---

```bash
ldapsearch -x -h ad.example.com -D 'vmail' -W -b 'cn=users,dc=example,dc=com'

postconf -e virtual_alias_maps=''
postconf -e sender_bcc_maps=''
postconf -e recipient_bcc_maps=''
postconf -e relay_domains=''
postconf -e relay_recipient_maps=''
postconf -e sender_dependent_relayhost_maps=''

postconf -e smtpd_sasl_local_domain='example.com'
postconf -e virtual_mailbox_domains='example.com'

postconf -e transport_maps='hash:/etc/postfix/transport'

postconf -e smtpd_sender_login_maps='proxy:ldap:/etc/postfix/ad_sender_login_maps.cf'
postconf -e virtual_mailbox_maps='proxy:ldap:/etc/postfix/ad_virtual_mailbox_maps.cf'
postconf -e virtual_alias_maps='proxy:ldap:/etc/postfix/ad_virtual_group_maps.cf'
```

Create/edit file: _/etc/postfix/transport_

```bash
postmap hash:/etc/postfix/transport
```

```bash
postmap -q user@example.com ldap:/etc/postfix/ad_virtual_mailbox_maps.cf
postmap -q user@example.com ldap:/etc/postfix/ad_sender_login_maps.cf
postmap -q testgroup@example.com ldap:/etc/postfix/ad_virtual_group_maps.cf
```

```bash
telnet localhost 143
```

* POP3 service: port 110 over TLS (recommended), or port 995 with SSL.
* IMAP service: port 143 over TLS (recommended), or port 993 with SSL.
* SMTP service: port 587 over TLS (recommended), or port 465 with SSL.
* CalDAV and CardDAV server addresses: https://<server>/SOGo/dav/<full email address>

```bash
USE_EXISTING_MYSQL='YES' \
    MYSQL_SERVER_ADDRESS='' \
    MYSQL_SERVER_PORT='3306' \
    MYSQL_ROOT_USER='' \
    MYSQL_ROOT_PASSWD='' \
    MYSQL_GRANT_HOST='' \
    bash iRedMail.sh
```

Dovecot

* %u - полное имя пользователя(с доменной частью: user@domail.local)
* %n - короткое имя пользователя(без доменной части: user)
* %d - доменная часть(domail.local), может быть пустой
* %h - домашний каталог, тоже может быть пустым

Postfix

* %d Доменная часть без локальной части и символа @ (например, test.org).
* %s Полный почтовый адрес (например, lena@test.org).
* %u Локальная часть без символа @ и указания домена (например, lena).
