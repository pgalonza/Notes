# MOUNT

###### cifs
```
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

# Network
###### Forward
```
echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.all.forwarding=1 >> /etc/sysctl.conf
```

# File, socket limits

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

###### Maximum queue size of packet
```
net.core.netdev_max_backlog =
```

###### Maximum number of open sockets waiting to be connected
```
net.core.somaxconn =
```

###### PAM limits configuration
_/etc/security/limits.conf_, _/etc/security/_
```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

###### _/etc/systemd/system.conf_, _/etc/systemd/user.conf_, */etc/systemd/<systemd_unit>/override.conf*
```
DefaultLimitNOFILE=
```

###### _/lib/systemd/system/<service>_, _/etc/systemd/*_, _/usr/lib/systemd/system/<service>_
```
LimitNOFILE=
```

# Swap

###### _/etc/sysctl.conf_
```
vm.swappiness=10
```

# Environment

_/etc/environment_
```
export PYTHONPATH=/data/libraries_and_modules/python
```

# TFTP
```
server_args             = -u tftpd -s /var/lib/tftpboot --verbose/-vvv
disable                 = no
```

# Django/CMS
```
pip install --upgrade virtualenv
virtualenv env
source env/bin/activate
(env) $ pip install djangocms-installer
(env) $ djangocms mysite
yum install python3-devel mysql-devel
pip3.6 install mysqlclient
python3.6 manage.py migrate
python3.6 manage.py runserver
python3.6 manage.py startapp firstapp
```

# PHP-FPM
```
rpm -Uhv http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum install yum-utils
yum-config-manager --enable remi-php71
yum install php71
yum install -y php-mysql php-mbstring php-mcrypt php-devel php-xml php-gd
```

# Kernels

###### Remove old kernels
```
yum install yum-utils
package-cleanup --oldkernels --count=2
```

###### Automatic remove old kernels
_/etc/yum.conf_
```
installonly_limit=3
```
