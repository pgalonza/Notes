---
title: System information
draft: false
description: "CLI commands for get System information"
---

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