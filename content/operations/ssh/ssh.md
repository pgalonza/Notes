---
title: "SSH"
draft: false
description: "SSH notes"
aliases:
  - /operations/linux/ssh/
---

{{< toc >}}

Remove all keys host from known_hosts

ssh-keygen -R <host_name>

Executing a command on a remote host

```bash
ssh user_name@remote_server "comamnd"
```

Copy directory

```bash
tar -cvj /datafolder | ssh user_name@remote_server "tar -xj -C /datafolder"
```

Wireshark

```bash
ssh user_name@remote_server 'tcpdump -c 1000 -nn -w - not port 22' | wireshark -k –i
```

Do not execute a remote command

```bash
ssh -N
```

Allows remote hosts to connect to local forwarded ports

```bash
ssh -g
```

Requests ssh to go to background just before command execution

```bash
ssh -f
```

Editing a file via scp

```bash
vim scp://user_name@remote_server //path_to_file
```

Mount local directory to remote host

```bash
sshfs user_name@remote_serve:/remote_directory /local_directory
```

Show control sequences

```bash
<Enter>~?
```

## SSH Keys

Generate RSA

```bash
ssh-keygen -f ~/name_key_file_rsa -t ed25519
```

Generate for paramiko

```bash
ssh-keygen -m pem -t rsa -C "test"
```

Convert for FileZilla

```bash
puttygen keyname -o keyname.ppk
```

Add fingerprint

```bash
ssh-keyscan -t <fingerprint type> -H <host_name> >> ~/.ssh/known_hosts
```

## SSH Certificates

### Host cetrificates

Generate key pair for host Certificate Authority (CA)

```bash
ssh-keygen -t rsa -b 4096 -f <host CA key file name>_rsa_key -C "<comment>"
```

Generate ssh key pair for target host

```bash
ssh-keygen -t rsa -b 4096 -f <host key file name>_rsa_key
```

Signing the host key

```bash
ssh-keygen -s <host CA key file name>_rsa_key -I "<key ID>" -h -n "<host principals>" -V <validity interval> <host ca key file name>_rsa_key.pub
ssh-keygen -Lf <host certificate file name>_rsa_key-cert.pub
```

Copy certificate and keys to target host

```bash
scp <host ca key file name>_rsa_key.pub <user_name>@<remote_server>:/etc/ssh
scp <host ca key file name>_rsa_key-cert.pub <user_name>@<remote_server>:/etc/ssh
scp <host ca key file name>_rsa_key <user_name>@<remote_server>:/etc/ssh
```

Add host certificate in sshd config __/etc/ssh/sshd_config__

```text
HostCertificate  /etc/ssh/<host ca key file name>_rsa_key-cert.pub
```

Add host CA certificate to known_hosts on user computer

```text
@cert-authority <wildcard domain> <content of pub key of Certificate Authority>
```

### User certificates

[Information from](https://goteleport.com/blog/how-to-configure-ssh-certificate-based-authentication/)

Generate key pair for user Certificate Authority (CA)

```bash
ssh-keygen -t rsa -b 4096 -f <user CA key file name>_rsa_key -C "<comment>"
```

Generate ssh key pair for target user

```bash
ssh-keygen -t rsa -b 4096 -f <user key file name>_rsa_key
```

Signing the user key

```bash
ssh-keygen -s <user CA key file name>_rsa_key -I "<key ID>" -h -n "<user principals>" -V <validity interval> <user ca key file name>_rsa_key.pub
ssh-keygen -Lf <user certificate file name>_rsa_key-cert.pub
```

Copy user user Certificate Authority (CA) to target host

```bash
scp <user ca key file name>_rsa_key.pub <user_name>@<remote_server>:/etc/ssh
```

Add user Certificate Authority (CA) in sshd config __/etc/ssh/sshd_config__

```text
TrustedUserCAKeys /etc/ssh/<user ca key file name>_rsa_key.pub
```

## SSH Tunneling

### SOCKS-proxy

local host > ssh host > Network

```bash
ssh -D 0.0.0.0:port_number user_name@remote_server
```

### Port forwarding

local host > ssh host

```bash
ssh -L 0.0.0.0:port_number:127.0.0.1:port_number user_name@remote_server
```

### Port forwarding to remote host

local host > ssh host > remote host

```bash
ssh -L 0.0.0.0:port_number:X.X.X.X:port_number user_name@remote_server
```

### Reverse ssh tunnel

ssh host > local host -> (local host > ssh host)

```bash
ssh -R 0.0.0.0:port_number:127.0.0.1:port_number user_name@remote_server
```

### Reverse ssh tunnel to remote host

remote host < ssh host > local host -> (local host > ssh host > remote host)

```bash
ssh -R 0.0.0.0:port_number:X.X.X.X:port_number user_name@remote_server
```

### Reverse SOCKS-proxy

Network < ssh host > local host -> (local host > ssh host > Network)

```bash
ssh -v -R 0.0.0.0:port_number user_name@remote_server
```

### Jumping through the remote hosts

local host > host1 > ssh host

```bash
ssh -J host1,host2,host3 user_name@remote_server
```

### Dual ssh tunnel

local host > ssh host
remote host > ssh_host

local_host > ssh_host > remote_host

```bash
ssh -L port_number:127.0.0.1:port_number user_name@remote_server
ssh -R port_number:127.0.0.1:port_number user_name@remote_server
```

## Banner

Create file

```bash
vim /etc/mybanner
```

Enable banner in _\/etc/ssh\/sshd_config_

```text
Banner /etc/mybanner
```

## X11

Install

```bash
yum install xauth
```

Run remote GUI-application

```bash
ssh -XYC remote_server program_name
```

## Configuration

```text
Host *
ForwardAgent no
ForwardX11 no
ForwardX11Trusted yes
Protocol 2
ServerAliveInterval 60
ServerAliveCountMax 30

Host <alias>
  HostName <host_name>
  User <user_name>
  port 22
  IdentityFile <path_to_key>

Host *
  User <user_name>
  port 22
  IdentityFile <path_to_key>
```
