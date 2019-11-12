# New installation
Mirror repository
```
https://mirror.yandex.ru/centos/8/BaseOS/x86_64/os/
```

Repository
```
yum/dnf install epel-release
```

Centos 7 packet
```
yum install net-tools iptables-services ipset-service
```

Packet Centos 7/8
```
yum/dnf wget vim htop tmux
```

No root ssh
```
echo "PermitRootLogin no" >> /etc/ssh/sshd_config
```

Change host name
```
hostnamectl set-hostname
```

Set default zone
```
firewall-cmd --set-default=internal
```

Disable selinux
_/etc/sysconfig/selinux_
```
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
systemctl reboot
```


Disable IPV6
```
echo net.ipv6.conf.all.disable_ipv6 = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.default.disable_ipv6 = 1 >> /etc/sysctl.conf
```

Java
```
yum/dnf -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel
```

## Centos 8
Activation the web console
```
systemctl enable --now cockpit.socket
```

## Zabbix agent

Zabbix repository
```
rpm -ivh http://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm
```

Zabbix user for mysql check
```
GRANT USAGE ON *.* TO 'zabbix'@'%' IDENTIFIED BY 'superpassword';
```

Make zabbix agent directory
```
mkdir /var/lib/zabbix
```

## Zabbix database
_/etc/sysctl.conf_
```
echo vm.swappiness = 10 >> /etc/sysctl.conf
```

_/etc/fstab_
```
defaults,noatime,nosuid,noexec,nodev 0 0
```

## MariaDB
```
yum/dnf install MariaDB-backup MariaDB-server MariaDB-client
```

## MOUNT

CIFS
```
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

## NGINX

Disable ignore invalid headers
```
echo "ignore_invalid_headers off;" >> /etc/nginx/nginx.conf
```

## PYTHON

Add repository
```
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
```
Install packages
```
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
```

## File limit

_/etc/sysctl.conf_

Maximum of objects inotify per user
```
fs.inotify.max_user_instances=
```

Maximum of watch files and directories per object inotify
```
fs.inotify.max_user_watches=
```

Maximum of events in queued
```
fs.inotify.max_queued_events=
```

Maximum of open descriptors
```
fs.file-max=
```

## PAM limits configuration

_/etc/security/limits.conf_
_/etc/security/_
```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

## Repository

Exclude packages
_/etc/yum.repos.d/_
```
Exclude=
```
