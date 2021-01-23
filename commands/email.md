# E-mail

## POSTFIX
Check configuration
```
postfix check
postconf
```

Queue view
```
mailq | less
postqueue -p | less
mailq | grep Request
find /var/spool/postfix/deferred -type f | wc -l
find /var/spool/postfix/active -type f | wc -l
find /var/spool/postfix/incoming -type f | wc –l
```

Queue send
```
postqueue -f
mailq -q
postsuper -r ALL
postqueue -i <ID-mail>
postsuper -r <ID-mail>
postqueue -s <domain>
```

Queue drop
```
postsuper -d ALL
postsuper -d deferred
postsuper -d <ID-mail>
```

Queue halt
```
postsuper -h <ID-mail>
postsuper -h ALL
postsuper -h deferred
```

Queue run
```
postsuper -H <ID-mail>
postsuper -H ALL
```


## Mail
Mail console client
```
mutt -f
```

Send mail
```
(echo  "Subject: test1"; echo "test2";)|sendmail -f sender@domain.com recipient@domain.com
```


## Dovecot
Quota
```
dovecot set quota
```

Reload the dovecot
```
doveadm reload
```

Show who connected
```
doveadm who -1
```

Clean the authorization cache
```
doveadm auth cache flush
```
