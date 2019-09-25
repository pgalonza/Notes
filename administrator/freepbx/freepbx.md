# General

###### Core FastAGI Server is not running
```
fwconsole setting LAUNCH_AGI_AS_FASTAGI 1
```

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


###### ODBC
_amportal.conf_
```
CDRDBHOST=10.0.198.46
CDRDBNAME=asteriskcdrdb
CDRDBPASS=EJkcxSQU
CDRDBPORT=3306
CDRDBTABLENAME=cdr
CDRDBTYPE=mysql
CDRDBUSER=freepbxuser
CDRUSEGMT=FALSE
```

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
*res_odbc_custom.conf*
```
[asteriskcdrdb]
enabled=>yes
dsn=>asteriskcdrdb
pooling=>no
limit=>5
```

_odbcinst.ini_
```
[MySQL]
Description     = ODBC for MySQL
Driver          = /usr/lib/libmyodbc5.so
Setup           = /usr/lib/libodbcmyS.so
Driver64        = /usr/lib64/libmyodbc5.so
Setup64         = /usr/lib64/libodbcmyS.so
FileUsage       = 1
```

Check connection
```
*CLI> odbc show
```

###### Yealink reload
_sip_notify_custom.conf_
```
[reboot-yealink]
Event=>check-sync\;reboot=true to Event=>check-sync\;reboot=false
```

###### Admin module
disabel
```
Contact Manager
Digium Addons
Online Support
REST API
iSymphonyV3
Directory
Do-Not-Disturb (DND)
Parking Lot
Wake Up Calls
DAHDi Config
Digium Phones Config
Google Voice/Chan Motif
SIPSTATION
WebRTC Phone
Weak Password Detection
Fax Configuration
Class of Service
PBX Upgrader
Phone Apps
XMPP
Zulu
AMD
Appointment Reminder
Broadcast
CallerID Managment
Conference Pro
Directory
Do-Not-Disturb (DND)
Paging Pro
Parking Pro
Queues Pro
Sangoma Property Management
Voicemail Notifications
Web Callback
Custom Contexts
Extension Routes
Outbound Call Limit
SMS
Vega
Call Recording Report
Pinsets Pro
Queue Reports
Queue Wallboard
Voicemail Reports
Customer Relationship Management
EndPoint Manager
Fax Configuration Professional
High Availability Services
OSS PBX End Point Manager
```
