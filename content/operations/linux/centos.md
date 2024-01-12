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

## DNF

Excluding package update

```ini
[main]
excludepkgs=<package names with comma separated>
```
