---
title: "FreePBX"
draft: false
---

## Core FastAGI Server is not running

```bash
fwconsole setting LAUNCH_AGI_AS_FASTAGI 1
```

## Number of characters in the display name field

_/var/www/html/admin/assets/js/pbxlib*_

```bash
function isCorrectLengthExtensions(s)
```

## Activation of text message

_sip_general_custom.conf_

```ini
accept_outofcall_message = yes
outofcall_message_context = messages
auth_message_requests = no
```

_Extensions_custom.conf_

```ini
[messages]
exten => _XXXXX,1,MessageSend(sip:${EXTEN},"${CALLERID(name)}"${MESSAGE(from)})
```

## Sounds

[Download](http://downloads.asterisk.org/pub/telephony/sounds/)

## Yealink reload

_sip_notify_custom.conf_

```ini
[reboot-yealink]
Event=>check-sync\;reboot=true to Event=>check-sync\;reboot=false
```

## Follow Me

Only for specific caller
_extensions_override_freepbx.conf_

```ini
exten => XXX,1,GotoIf($[(${DB_EXISTS(AMPUSER/${EXTEN}/followme/ddial)} != 1 | "${DB(AMPUSER/${EXTEN}/followme/ddial)}" = "EXTENSION") | ${CALLERID(num)} != XXXX]?ext-local,${EXTEN},1:followme-check,${EXTEN},1)
```

## Admin module

### Disabel

```text
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

## Update

Change the asterisk version

```bash
asterisk-version-switch
```
