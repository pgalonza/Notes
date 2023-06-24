---
title: "Install Centos"
draft: false
---

{{< toc >}}

Mirror repository

```text
https://mirror.yandex.ru/centos/
```

Repository

```bash
yum/dnf install epel-release
```

Packet

```bash
yum/dnf wget vim htop tmux
```

No root ssh

```bash
echo "PermitRootLogin no" >> /etc/ssh/sshd_config
```

Change host name

```bash
hostnamectl set-hostname
```

Set default zone

```bash
firewall-cmd --set-default=internal
```

Disable selinux
_/etc/sysconfig/selinux_

```bash
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
systemctl reboot
```

Disable IPV6

```bash
echo net.ipv6.conf.all.disable_ipv6 = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.default.disable_ipv6 = 1 >> /etc/sysctl.conf
```

## Centos 8

Activation the web console

```bash
systemctl enable --now cockpit.socket
```

## MariaDB

https://downloads.mariadb.org/MariaDB/repositories/#mirror=netinch

```bash
yum/dnf install MariaDB-backup MariaDB-server MariaDB-client
```

## File limit

_/etc/sysctl.conf_

Maximum of objects inotify per user

```text
fs.inotify.max_user_instances=
```

Maximum of watch files and directories per object inotify

```text
fs.inotify.max_user_watches=
```

Maximum of events in queued

```text
fs.inotify.max_queued_events=
```

Maximum of open descriptors

```text
fs.file-max=
```

## PAM limits configuration

_/etc/security/limits.conf_
_/etc/security/_

```text
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

## Repository

Exclude packages
_/etc/yum.repos.d/_

```text
Exclude=
```
