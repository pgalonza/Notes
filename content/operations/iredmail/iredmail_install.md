---
title: "Install iRedMail"
draft: false
---

Check ldap connection

```bash
ldapsearch -x -h ad.example.com -D 'vmail' -W -b 'cn=users,dc=example,dc=com'
```

Flush unwanted parameters

```bash
postconf -e virtual_alias_maps=''
postconf -e sender_bcc_maps=''
postconf -e recipient_bcc_maps=''
postconf -e relay_domains=''
postconf -e relay_recipient_maps=''
postconf -e sender_dependent_relayhost_maps=''
```

Set mail domain

```bash
postconf -e smtpd_sasl_local_domain='example.com'
postconf -e virtual_mailbox_domains='example.com'
```

Set transport file

```bash
postconf -e transport_maps='hash:/etc/postfix/transport'
```

Set maps

```bash
postconf -e smtpd_sender_login_maps='proxy:ldap:/etc/postfix/ad_sender_login_maps.cf'
postconf -e virtual_mailbox_maps='proxy:ldap:/etc/postfix/ad_virtual_mailbox_maps.cf'
postconf -e virtual_alias_maps='proxy:ldap:/etc/postfix/ad_virtual_group_maps.cf'
```

Create the transport file
_/etc/postfix/transport_

Hash postfix transport

```bash
postmap hash:/etc/postfix/transport
```

Check user mailbox

```bash
postmap -q user@example.com ldap:/etc/postfix/ad_virtual_mailbox_maps.cf
```

Check user account

```bash
postmap -q user@example.com ldap:/etc/postfix/ad_sender_login_maps.cf
```

Check groups of mailing

```bash
postmap -q testgroup@example.com ldap:/etc/postfix/ad_virtual_group_maps.cf
```
