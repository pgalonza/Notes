---
title: System information
draft: false
description: "Essential Linux system information commands: CPU, memory, block devices, kernel modules, distribution details, reboot history, and hardware topology for quick diagnostics and monitoring."
summary: "A handy reference of command‑line tools to gather detailed system insights, from hardware topology to OS version and reboot logs."
---

## Locale

Set global

```bash
localectl set-locale <locale variable>=<locale value>
vim /etc/locale.conf
```

Set for user

```bash
export <locale variable>=<locale value>
```

Print real and effective user and group IDs

```bash
id
```

Show who is logged on and what they are doing

```bash
w
```

Show list block devices

```bash
lsblk
```

Display information about the CPU architecture

```bash
lscpu
```

Show the topology of the system

```bash
lstopo
```

Display amount of free and used memory in the system

```bash
free -h
```

Show certain LSB (Linux Standard Base) and Distribution information.

```bash
lsb_release -a
```

Show distribution information.

```basg
cat /etc/*-release
cat /proc/version
cat /etc/issue
```

Show the status of modules in the Linux Kernel

```bash
lsmod
```

Show Posix IPC

```bash
ipcs -ma
```

Get distribution ID

<https://unix.stackexchange.com/a/432819/440845>

```bash
awk -F= '$1=="ID" { print $2 ;}' /etc/os-release | sed s/\"//g
```

Information about commands

```bash
command -v <command>
type <command>
type -t <command>
type -a <command>
```

Show the system shutdown entries and run level changes.

[Information from](https://geekflare.com/check-linux-reboot-reason/)

```bash
who -b
last -xF | head | tac
ausearch -i -m system_boot,system_shutdown | tail -4
```

```bash
journalctl --list-boots
journalctl -b <reboot id> -n
```

```bash
journalctl | grep -i "reboot\|shutdown"
grep -i "reboot\|shutdown" /var/log/messages
```

Show CPU caches

```bash
lscpu --caches
```

Collect all information about the system

[Kaspersky collect information script](https://box.kaspersky.com/f/00a1a6d8beb24554a72d/?dl=1)

## Limits

Get name and path byte limits

```bash
getconf -a | grep -i name_max
getconf -a | grep -i path_max
```

## Documentation

```bash
/usr/share/doc
```

## Time

View system time

```bash
timedatectl status
```

## Memory

Memory use

```bash
cat /proc/meminfo

ps axo rss,comm,pid \
| awk '{ proc_list[$2]++; proc_list[$2 "," 1] += $1; } \
END { for (proc in proc_list) { printf("%d\t%s\n", \
proc_list[proc "," 1],proc); }}' | sort -n | tail -n 10 | sort -rn \
| awk '{$1/=1024;printf "%.0fMB\t",$1}{print $2}'
```

## Udevadm

Show in realtime

```bash
udevadm monitor
```

Get attributes

```bash
udevadm info /dev/sdb1
```
