---
title: "Other"
draft: false
description: "Linux shutdown, reboot, poweroff commands, logrotate configuration, and Certbot SSL certificate management."
summary: "Shutdown/poweroff/reboot commands, logrotate check, and Certbot SSL certificate creation and renewal."
---

{{< toc >}}

## Shutdown/Poweroff/Reboot

* Shutdown

```bash
shutdown -h hours:minutes
init 0
telinit 0
shutdown -h now
poweroff
halt --poweroff
reboot --poweroff
shytdown --poweroff
halt --no-wtmp --no-wall
```

 Cancel

```bash
shutdown -c
```

* Poweroff

```bash
halt
halt --force
reboot --halt
poweroff --halt
poweroff --force
```

* Reboot

```bash
poweroff --reboot
shutdown --reboot
reboot --force
halt --reboot
init 6
reboot
```

Problems with software

```bash
reboot -f
```

Problems with kernel, mount, libc

```bash
echo b>/proc/sysrq-trigger
```

Problems with kernel and hardware

```bash
ipmitool chassis power cycle
```

Problems with kernel and hardware without open console

```bash
ipmitool -H ipmi.server.local chassis power cycle
```


## Logrotate

Check the configuration file

```bash
logrotate -d /etc/logrotate.d/config_name
````


## Certbot

Create certificate
_certbot.ini_

```bash
authenticator = standalone
noninteractive = true
agree-tos = true
rsa-key-size = 2048
```

```bash
certbot certonly --config ./certbot.ini --email <e-mail address> --work-dir </var/lib/letsencrypt> --config-dir <where save data> --domain <domain_name>
```

Renew certificate

```bash
certbot renew --work-dir </var/lib/letsencrypt> --config-dir <where save data>
```

