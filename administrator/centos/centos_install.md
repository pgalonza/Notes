# New installation
Mirror repository
```
https://mirror.yandex.ru/centos/8/BaseOS/x86_64/os/
```

Centos 7 repository
```
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
```

Centos 8 repository
```
dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
```

Repository
```
yum/dnf install epel-release
```

Centos 7 packet
```
yum install net-tools iptables-services ipset-service
```

Packet
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
https://downloads.mariadb.org/MariaDB/repositories/#mirror=netinch
```
yum/dnf install MariaDB-backup MariaDB-server MariaDB-client
```

## PostgreSQL
https://yum.postgresql.org
```
yum/dnf install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install postgresql postgresqlXX-server
/usr/pgsql-11/bin/postgresql-XX-setup initdb
passwd postgres
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

## Python
Add repository ius
```
sudo yum install https://$(rpm -E '%{?centos:centos}%{!?centos:rhel}%{rhel}').iuscommunity.org/ius-release.rpm

sudo yum install \
https://repo.ius.io/ius-release-el7.rpm \
https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

Add repository scl
```
sudo yum install centos-release-scl
```

Install packages
```
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
```

PIP install
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
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

## Docker
Repository
```
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

Stable
```
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

Install
```
yum install docker-ce docker-ce-cli containerd.io
```
