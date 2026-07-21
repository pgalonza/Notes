---
title: Shutdown, Poweroff, Reboot
draft: false
description: "Linux shutdown, poweroff, and reboot commands for system administration and troubleshooting."
summary: "A reference of commands for shutting down, powering off, and rebooting Linux systems, including forced reboot and IPMI power cycle."
---

{{< toc >}}

## Shutdown

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

## Poweroff

```bash
halt
halt --force
reboot --halt
poweroff --halt
poweroff --force
```

## Reboot

```bash
poweroff --reboot
shutdown --reboot
reboot --force
halt --reboot
init 6
reboot
```

## Problems with software

```bash
reboot -f
```

## Problems with kernel, mount, libc

```bash
echo b > /proc/sysrq-trigger
```

## Problems with kernel and hardware

```bash
ipmitool chassis power cycle
```

## Problems with kernel and hardware without open console

```bash
ipmitool -H ipmi.server.local chassis power cycle
```