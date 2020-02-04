# Centos
## MOUNT
CIFS
```
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

## Network
Forward
```
echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.all.forwarding=1 >> /etc/sysctl.conf
```

IPv6
_/etc/sysconfig/network_
```
NETWORKING_IPV6=yes
```

_/etc/sysconfig/network-scripts/_
```
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
```
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
```
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
```
modprobe --first-time 8021q
```

_/etc/sysconfig/network-scripts/ifcfg-enpX_
```
TYPE=Ethernet
NAME=
DEVICE=
ONBOOT=yes
UUID=
```

_/etc/sysconfig/network-scripts/ifcfg-enpX.X_
```
TYPE=VLAN
ONBOOT=yes
VLAN_ID=
VLAN=yes
DEVICE=enpX.X
```

## File, socket limits
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

Maximum queue size of packet
```
net.core.netdev_max_backlog =
```

Maximum number of open sockets waiting to be connected
```
net.core.somaxconn =
```

## PAM limits configuration
_/etc/security/limits.conf_, _/etc/security/_
```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

_/etc/systemd/system.conf_, _/etc/systemd/user.conf_,  _/etc/systemd/<systemd_unit>/override.conf_
```
DefaultLimitNOFILE=
```

_/lib/systemd/system/<service>_, _/etc/systemd/*_, _/usr/lib/systemd/system/<service>_
```
LimitNOFILE=
```

_override.conf_
```
mkdir /etc/systemd/system/service_name.service.d/
```
```
[Service]
LimitNOFILE=100000
```

## Swap

_/etc/sysctl.conf_
```
vm.swappiness=10
```

## Environment

_/etc/environment_
```
export PYTHONPATH=/data/libraries_and_modules/python
```

## TFTP
```
server_args             = -u tftpd -s /var/lib/tftpboot --verbose/-vvv
disable                 = no
```

## Django/CMS
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

## PHP-FPM
```
rpm -Uhv http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum install yum-utils
yum-config-manager --enable remi-php71
yum install php71
yum install -y php-mysql php-mbstring php-mcrypt php-devel php-xml php-gd
```

## Kernels
 Remove old kernels
```
yum install yum-utils
package-cleanup --oldkernels --count=2
```

Automatic remove old kernels
_/etc/yum.conf_
```
installonly_limit=3
```

## Systemd
### Searach problem
Show problems
```
systemctl --failed
```

Get pid
```
systemctl status systemd-modules-load
```

Show problems by pid
```
journalctl _PID=
```

## SSL
### Certificate Authority (CA)
Install openssl
```
yum/dnf install -y openssl
```

Generate a private key
```
cd /etc/pki/CA/private/
openssl genrsa -aes128 -out name-CA.key 2048/4096
```

Create a Certificate Authority (CA) certificate
```
openssl req -new -x509 -days 1825 \
-key /etc/pki/CA/private/name-CA.key \
-out /etc/pki/CA/certs/name-CA.crt
```

Generate a CSR (Certificate Signing Request) for server1
```
openssl genrsa -out /etc/pki/tls/private/web-01.key 1024/2048/4096
openssl req -new -key /etc/pki/tls/private/web-01.key \
-out /etc/pki/tls/server1.csr
scp /etc/pki/tls/server1.csr server-ca:~/server1.csr
```

Sign the CSR by Certificate Authority (CA)
```
openssl x509 -req -in server1.csr \
-CA /etc/pki/CA/certs/name-CA.crt \
-CAkey /etc/pki/CA/private/name-CA.key \
-CAcreateserial \
-out server1.crt \
-days 1828

cat coturn1.key coturn1.crt > coturn1.pem

scp server1.* server1:/etc/pki/tls/certs/
```

## SysRq
Enable
* On work
```
sysctl kernel.sysrq=1
echo "1" > /proc/sys/kernel/sysrq
```

* On boot
```
echo "kernel.sysrq = 1" >> /etc/sysctl.d/99-sysctl.conf
```

* Before mounting and ini

_Kernel_
```
sysrq_always_enabled=1
```

## Sudoers
_/etc/sudoers_
Write logs
```
Defaults  log_host, log_year, logfile="/var/log/sudo.log"
```

Run command with sudo without password
```
notify ALL=(ALL) NOPASSWD:path_to_command, path_to_command
```

## Entropy
Install
```
yum/dnf install haveged
```

Start
```
systemctl enable haveged
systemctl start haveged
```
