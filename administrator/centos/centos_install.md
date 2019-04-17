# New installation

###### Packet
```
yum install epel-release net-tools wget vim htop tmux
```

###### No root ssh
```
echo "PermitRootLogin no" >> /etc/ssh/sshd_config
```

###### Change host name
```
hostnamectl set-hostname
```

###### Set default zone
```
firewall-cmd --set-default=internal
```

###### Disable selinux
_/etc/sysconfig/selinux_

###### Disable IPV6
```
echo net.ipv6.conf.all.disable_ipv6 = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.default.disable_ipv6 = 1 >> /etc/sysctl.conf
```

###### Java
```
yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel
```

# Zabbix agent

###### Zabbix repository
```
rpm -ivh https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
```

###### Zabbix user for mysql check
```
GRANT USAGE ON *.* TO 'zabbix'@'%' IDENTIFIED BY 'superpassword';
```

###### Make zabbix agent directoru
```
mkdir /var/lib/zabbix
```

# Zabbix database
_/etc/sysctl.conf_
```
vm.swappiness=10
```

_/etc/fstab_
```
defaults,noatime,nosuid,noexec,nodev 0 0
```

# MariaDB
```
yum install MariaDB-backup MariaDB-server MariaDB-client
```

# MOUNT

###### CIFS
```
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

# NGINX

###### Disable ignore invalid headers
```
echo "ignore_invalid_headers off;" >> /etc/nginx/nginx.conf
```

# PYTHON

###### Add repository
```
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
```
###### Install packages
```
sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
```

# File limit

_/etc/sysctl.conf_

###### Maximum of objects inotify per user
```
fs.inotify.max_user_instances=
```

###### Maximum of watch files and directories per object inotify
```
fs.inotify.max_user_watches=
```

###### Maximum of events in queued
```
fs.inotify.max_queued_events=
```

###### Maximum of open descriptors
```
fs.file-max=
```

###### PAM limits configuration

_/etc/security/limits.conf_
_/etc/security/_
```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

# Repository

###### Exclude packages
_/etc/yum.repos.d/_
```
Exclude=
```
