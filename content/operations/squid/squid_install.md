---
title: "SQUID"
draft: false
---

```bash
wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz
wget http://www.squid-cache.org/Versions/v4/squid-4.6.tar.gz
```

Install tools and pachages

```bash
yum group install "Development Tools"
yum install -y perl gcc autoconf automake make sudo wget
yum install libxml2-devel libcap-devel
yum install libtool-ltdl-devel openssl-devel
```

Extract source

```bash
tar xvf squid-4.6.tar.gz
tar -zxf openssl-1.1.1b.tar.gz
```

Show configuration options

```bash
./configure -help | less
```

Configure openssl and install

```bash
./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl shared zlib
make
make install
make install_sw
```

Add path /usr/local/openssl/lib
_/etc/ld.so.conf.d/openssl.conf_

```bash
ldconfig
ldd /usr/bin/openssl
```

Configure squid and install

```bash
./configure --with-default-user=squid --with-pidfile=/var/run/squid/squid.pid --with-logdir=/var/log/squid --prefix=/usr --includedir=/usr/include --datadir=/usr/share --bindir=/usr/sbin --libexecdir=/usr/lib/squid --localstatedir=/var --sysconfdir=/etc/squid --with-openssl=/usr/local/openssl --enable-ssl --enable-ssl-crtd --enable-delay-pools --enable-linux-netfilter --enable-basic-auth-helpers="negotiate_kerberos_auth" --enable-auth-negotiate=kerberos --with-pthreads --with-libcap --disable-ipv6
make
make install
```

Systemctl

```bash
squid-4.6/tools/systemd/squid.service /usr/lib/systemd/system/
```

Create KEY

```bash
openssl req -new -newkey rsa:2048 -sha256 -days 1095 -nodes -x509 -extensions v3_ca -keyout proxyCA.pem  -out proxyCA.pem
```

Convert for windows clients

```bash
openssl x509 -in proxyCA.pem -outform DER -out proxyCA.der
```

Import certificate to local storage
_/etc/squid/*.der_ _ /etc/pki/ca-trust/source/anchors/_

```bash
update-ca-trust
```

Createcertificate storage

```bash
/usr/lib/squid/security_file_certgen -c -s /var/lib/ssl_db -M 4MB
chown squid:squid /var/lib/ssl_db
```

# Troubleshooting

## FATAL: Ipc::Mem::Segment::create failed to shm_open(/squid-cf__metadata.shm): (17) File exists

```bash
chown squid:squid /dev/shm/*
```

```bash
squid -k parse
```

Create the swap directories

```bash
squid -z
```

Start Squid

```bash
squid -NCd1
```

Check Squid

```bash
squidclient http://www.netscape.com/ > test
squid -k check
```
