---
title: "Install asterisk"
draft: false
---

## Libraries

Essential Libraries

```text
libjansson
libsqlite3
libxml2
libxslt
ncurses
openssl
uuid
```

Core Libraries

```text
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

## Packet

Compile

```bash
yum install make gcc gcc-c++ patch pkgconfig
```

Kernel

```bash
yum install kernel kernel-devel kernel-headers
```

Audio

```bash
yum install speex-devel speexdsp-devel libogg-devel libvorbis-devel lame
```

Lua

```bash
yum install lua-devel
```

Database

```bash
yum install mariadb-devel unixODBC-devel unixODBC mysql-connector-odbc sqlite-devel
```

Fax

```bash
yum install spandsp-devel
```

SSL/TLS

```bash
yum install openssl-devel libsrtp-devel
```

Other

```bash
yum install libxml2-devel libuuid-devel jansson-devel bzip2 zlib-devel libedit-devel subversion gsm-devel python-devel libcurl-devel
```

## Get source

Create work directory

```bash
mkdir /usr/src/asterisk
```

Asterisk 16

```bash
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-16-current.tar.gz
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-16-current-patch.tar.gz
```

Only if asterisk 13

```bash
wget http://www.digip.org/jansson/releases/jansson-2.12.tar.gz
wget https://www.pjsip.org/release/2.9/pjproject-2.9.tar.bz2
```

DAHDI

```bash
wget https://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-3.0.0.tar.gz
wget https://downloads.asterisk.org/pub/telephony/libpri/libpri-current.tar.gz
```

## Extract

gz

```bash
tar -zxvf
```

bz2

```bash
tar -xvjf
```

## MP3 support

```bash
./contrib/scripts/get_mp3_source.sh
```

## Resolve !all! of the dependencies

Install

```bash
contrib/scripts/install_prereq install
```

View

```bash
contrib/scripts/install_prereq test
```

## Build, compile and install

DAHDI

```bash
make all
make install
make config
```

LibPRI

```bash
make
make install
```

Asterisk

```bash
./configure --libdir=/usr/lib64 --with-jansson-bundled
make menuselect
make
make install
make config
make install-logrotate
```

## Firewalld

```bash
firewall-cmd --zone="name of zone" --permanent --add-service={sip,sips}
firewall-cmd --zone="name of zone" --permanent --add-port=2727/udp
irewall-cmd --zone="name of zone" --permanent --add-port=10000-20000/udp
firewall-cmd --zone="name of zone" --permanent --add-port=4569/udp
```

## Asterisk user and premissions

```bash
useradd asterisk -c "Asterisk User" -s /sbin/nologin -M
chown asterisk.asterisk /var/run/asterisk
chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk
```

_/etc/asterisk/asterisk.conf_

```ini
[options]
runuser = asterisk
rungroup = asterisk
```

_/etc/sysconfig/asterisk_

```ini
AST_USER="asterisk"
AST_GROUP="asterisk"
```

_/etc/udev/rules.d/dahdi.rules_

```ini
SUBSYSTEM="dahdi",OWNER="asterisk",GROUP="asterisk", MODE="0660"
```
