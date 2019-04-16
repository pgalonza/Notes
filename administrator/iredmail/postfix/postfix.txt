_ad_sender_login_maps.cf_
```
server_host     = host
server_port     = 389
version         = 3
bind            = yes
start_tls       = no
bind_dn         = user
bind_pw         = password
search_base     = dc=,dc=,dc=
scope           = sub
query_filter    = (&(|(mail=%s)(userPrincipalName=%s))(objectCategory=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
result_attribute= mail
debuglevel      = 0
```

_ad_virtual_group_maps.cf_
````
server_host     = host
server_port     = 389
version         = 3
bind            = yes
start_tls       = no
bind_dn         = user
bind_pw         = password
search_base     = dc=,dc=,dc=
scope           = sub
query_filter    = (&(objectCategory=group)(mail=%s))
special_result_attribute = member
leaf_result_attribute = mail
#result_attribute= userPrincipalName
debuglevel      = 0
```

_ad_virtual_mailbox_maps.cf_
```
server_host     = host
server_port     = 389
version         = 3
bind            = yes
start_tls       = no
bind_dn         = user
bind_pw         = password
search_base     = dc=,dc=,dc=
scope           = sub
query_filter    = (&(objectCategory=person)(mail=%s)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
result_attribute= mail
result_format   = %d/%u/Maildir/
debuglevel      = 0
```

_main.cf_
```
myhostname = host
myorigin = $mydomain
mydomain = mail_domain
mydestination = $myhostname, localhost.$mydomain, localhost, localhost.localdomain
virtual_mailbox_domains = mail_domain
dovecot_destination_recipient_limit = 1
smtpd_sasl_local_domain = mail_domain
message_size_limit = 52428800
inet_protocols = ipv4
mynetworks = 127.0.0.1 [::1] 10.0.0.0/16 172.16.0.0/12
```

###### Queue
```
bounce_queue_lifetime = 7d
maximal_queue_lifetime = 7d
minimal_backoff_time = 3h
maximal_backoff_time = 9h
queue_run_delay = 3m
```

###### Transport
```
.mail_domain dovecot
mail_domain dovecot
*      error:mail for local use only
```
