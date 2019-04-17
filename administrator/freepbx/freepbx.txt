###### Number of characters in the display name field

_/var/www/html/admin/assets/js/pbxlib*_

```
function isCorrectLengthExtensions(s)
```

###### Activation of text message

*sip_general_custom.conf*
```
accept_outofcall_message = yes
outofcall_message_context = messages
auth_message_requests = no
```

*Extensions_custom.conf*
```
[messages]
exten => _XXXXX,1,MessageSend(sip:${EXTEN},"${CALLERID(name)}"${MESSAGE(from)})
```

###### Sounds
[Download](http://downloads.asterisk.org/pub/telephony/sounds/)


_odbc.ini_
```
Description=
Driver=MySQL
Server=
Database=
User=
Password=
Port=3306
Socket=/var/lib/mysql/mysql.sock
Option=3
Charset=utf8
```

*cdr_mysql.conf*
```
[global]
hostname=
dbname=
table=cdr
password=
user=
port=3306
```
_cdr.conf_
```
enable=yes
```
