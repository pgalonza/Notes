---
title: "Centos"
draft: false
---

{{< toc >}}

## Network

_/etc/sysconfig/network-scripts/_

```text
TYPE=Ethernet
PROXY_METHOD=static
BROWSER_ONLY=no
BOOTPROTO=none
IPV6_AUTOCONF=no
DEFROUTE=yes
IPV6INIT=yes
IPV6ADDR=
IPV6_DEFAULTGW=
IPV6_PRIVACY=no
DNS0=""
DNS1=""
DNS2=""
DOMAIN=""
```

IPv4 static
_/etc/sysconfig/network-scripts/_

```text
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NAME=""
UUID=""
DEVICE=""
ONBOOT=yes
IPADDR=
PREFIX=
#NETMASK=
GATEWAY=
DNS1=
DNS2=
DOMAIN=
ZONE=internal
```

IPv4 dinamic
_/etc/sysconfig/network-scripts/_

```text
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NAME=
UUID=
DEVICE=
ONBOOT=yes
ZONE=internal
```

VLAN

```bash
modprobe --first-time 8021q
```

_/etc/sysconfig/network-scripts/ifcfg-enpX_

```text
TYPE=Ethernet
NAME=
DEVICE=
ONBOOT=yes
UUID=
```

_/etc/sysconfig/network-scripts/ifcfg-enpX.X_

```text
TYPE=VLAN
ONBOOT=yes
VLAN=yes
DEVICE=enpX.X
```

_/etc/sysconfig/network-scripts/ifcfg-vlanX_

```text
ONBOOT=yes
TYPE=VLAN
VLAN=yes
VLAN_NAME_TYPE=VLAN_PLUS_VID_NO_PAD
DEVICE=vlan5
PHYSDEV=ens32
VLAN_ID=5
```

Bridge
_/etc/sysconfig/network-scripts/ifcfg-brX_

```text
DEVICE=
TYPE=Bridge
ONBOOT=yes
BOOTPROTO=none
IPV6INIT=no
IPV6_AUTOCONF=no
DELAY=5
STP=yes
```

_/etc/sysconfig/network-scripts/ifcfg-enpX_

```text
DEVICE=enpX
BOOTPROTO=none
TYPE=Ethernet
NAME=
DEVICE=
ONBOOT=yes
UUID=
HOTPLUG=no
BRIDGE=brX
```

## File, socket limits

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

Maximum queue size of packet

```text
net.core.netdev_max_backlog =
```

Maximum number of open sockets waiting to be connected

```text
net.core.somaxconn =
```

## Environment

_/etc/environment_

```bash
export PYTHONPATH=/data/libraries_and_modules/python
```

## TFTP

```text
server_args             = -u tftpd -s /var/lib/tftpboot --verbose/-vvv
disable                 = no
```

## PHP-FPM

```bash
rpm -Uhv http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum install yum-utils
yum-config-manager --enable remi-php72
yum install php72
yum install -y php-mysql php-mbstring php-mcrypt php-devel php-xml php-gd
```

## Kernels

Remove old kernels

```bash
yum install yum-utils
package-cleanup --oldkernels --count=2
```

Automatic remove old kernels
_/etc/yum.conf_

```text
installonly_limit=3
```

## SysRq

Enable

* On work

    ```bash
    sysctl kernel.sysrq=1
    echo "1" > /proc/sys/kernel/sysrq
    ```

* On boot

    ```bash
    echo "kernel.sysrq = 1" >> /etc/sysctl.d/99-sysctl.conf
    ```

* Before mounting and ini

    _Kernel_

    ```text
    sysrq_always_enabled=1
    ```

## Sudoers

_/etc/sudoers_
Write logs

```text
Defaults  log_host, log_year, logfile="/var/log/sudo.log"
```

Run command with sudo without password

```text
notify ALL=(ALL) NOPASSWD:path_to_command, path_to_command
```

## Entropy

Install

```bash
yum/dnf install haveged
```

Start

```bash
systemctl enable haveged
systemctl start haveged
```
