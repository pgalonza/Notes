---
title: "OpenVPN"
draft: false
---

{{< toc >}}

## Install

Package

```bash
yum -y install openvpn unzip zip
```

Create the directory for keys

```bash
mkdir /etc/openvpn/keys
```

Download Easy-RSA

```bash
cd /etc/openvpn/keys
wget https://github.com/OpenVPN/easy-rsa/archive/master.zip
```

Create the PKI-keys structure

```bash
unzip master.zip
cd /etc/openvpn/keys/easy-rsa-master/easyrsa3
mv vars.example vars
./easyrsa init-pki
```

Create verification center CA

```bash
./easyrsa build-ca
```

Create the certificate request for server without password

```bash
./easyrsa gen-req server nopass
```

Sign a request for a certificate

```bash
./easyrsa sign-req server server
```

Diffie–Hellman

```bash
./easyrsa gen-dh
```

Copy keys to folder _openvpn_

```bash
cp pki/ca.crt /etc/openvpn/ca.crt
cp pki/dh.pem /etc/openvpn/dh.pem
cp pki/issued/server.crt /etc/openvpn/server.crt
cp pki/private/server.key /etc/openvpn/server.key
```

Create the key for client

```bash
./easyrsa gen-req client nopass
./easyrsa sign-req client client
```

Check the key

```bash
openssl verify -CAfile pki/ca.crt pki/issued/client.crt
```

Create folders for _log_ and _ccd_

```bash
mkdir /etc/openvpn/ccd && mkdir /var/log/openvpn
```

Create the configuration file for client
_/etc/openvpn/ccd/client_

```text
iroute 192.168.20.0 255.255.255.0
```
