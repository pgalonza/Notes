# New installation

###### Libraries
Essential Libraries
```
libjansson
libsqlite3
libxml2
libxslt
ncurses
openssl
uuid
```

Core Libraries
```
DAHDI
pjproject
unixodbc
libspeex
libspeexdsp
libresample
libcurl3
libvorbis
libogg
libsrtp
libical
libiksemel
libneon
libgmime
libunbound
```

###### Packet
Compile
```
yum install make gcc gcc-c++ patch pkgconfig
```

Kernel
```
yum install kernel kernel-devel kernel-headers
```

Audio
```
yum install speex-devel speexdsp-devel libogg-devel libvorbis-devel lame
```

Lua
```
yum install lua-devel
```

Database
```
yum install mariadb-devel unixODBC-devel unixODBC mysql-connector-odbc sqlite-devel
```

Fax
```
yum install spandsp-devel
```

SSL/TLS
```
yum install openssl-devel libsrtp-devel
```

Other
```
yum install libxml2-devel libuuid-devel jansson-devel bzip2 zlib-devel libedit-devel subversion gsm-devel python-devel libcurl-devel
```

###### Get source

Asterisk 16
```
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-16-current.tar.gz
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-16-current-patch.tar.gz

```

Only if asterisk 13
```
wget http://www.digip.org/jansson/releases/jansson-2.12.tar.gz
wget https://www.pjsip.org/release/2.9/pjproject-2.9.tar.bz2
```

DAHDI
```
wget https://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-3.0.0.tar.gz
wget https://downloads.asterisk.org/pub/telephony/libpri/libpri-current.tar.gz
```

###### Extract
gz
```
tar -zxvf
```

bz2
```
tar -xvjf
```

###### MP3 support
```
./contrib/scripts/get_mp3_source.sh
```

###### Resolve !all! of the dependencies
Install
```
contrib/scripts/install_prereq install
```

View
```
contrib/scripts/install_prereq test
```

###### Build compile and install
```
./configure --libdir=/usr/lib64 --with-jansson-bundled
make menuselect
make
make install
make config
make install-logrotate
```

###### Firewalld
```
firewall-cmd --zone="name of zone" --permanent --add-service={sip,sips}
firewall-cmd --zone="name of zone" --permanent --add-port=2727/udp
irewall-cmd --zone="name of zone" --permanent --add-port=10000-20000/udp
firewall-cmd --zone="name of zone" --permanent --add-port=4569/udp
```

###### Asterisk user and premissions
```
useradd asterisk -c "Asterisk User" -s /sbin/nologin -M
chown asterisk.asterisk /var/run/asterisk
chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk
```

_/etc/asterisk/asterisk.conf_
```
[options]
runuser = asterisk
rungroup = asterisk
```

_/etc/sysconfig/asterisk_
```
AST_USER="asterisk"
AST_GROUP="asterisk"
```

_/etc/udev/rules.d/dahdi.rules_
```
SUBSYSTEM=="dahdi",OWNER="asterisk",GROUP="asterisk", MODE="0660"
```
