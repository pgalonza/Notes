# IredMail install

######  Check ldap connection
```
ldapsearch -x -h ad.example.com -D 'vmail' -W -b 'cn=users,dc=example,dc=com'
```

###### Flush unwanted parameters
```
postconf -e virtual_alias_maps=''
postconf -e sender_bcc_maps=''
postconf -e recipient_bcc_maps=''
postconf -e relay_domains=''
postconf -e relay_recipient_maps=''
postconf -e sender_dependent_relayhost_maps=''
```

###### Set mail domain
```
postconf -e smtpd_sasl_local_domain='example.com'
postconf -e virtual_mailbox_domains='example.com'
```

###### Set transport file
````
postconf -e transport_maps='hash:/etc/postfix/transport'
```

###### Set maps
```
postconf -e smtpd_sender_login_maps='proxy:ldap:/etc/postfix/ad_sender_login_maps.cf'
postconf -e virtual_mailbox_maps='proxy:ldap:/etc/postfix/ad_virtual_mailbox_maps.cf'
postconf -e virtual_alias_maps='proxy:ldap:/etc/postfix/ad_virtual_group_maps.cf'
```

###### Create the transport file

_/etc/postfix/transport_


###### Hash postfix transport
```
postmap hash:/etc/postfix/transport
```

###### Check user mailbox
```
postmap -q user@example.com ldap:/etc/postfix/ad_virtual_mailbox_maps.cf
```

###### Check user account
```
postmap -q user@example.com ldap:/etc/postfix/ad_sender_login_maps.cf
```

##### Check groups of mailing
```
postmap -q testgroup@example.com ldap:/etc/postfix/ad_virtual_group_maps.cf
```
