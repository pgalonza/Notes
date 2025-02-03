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

## SSH Keys

Generate RSA

```bash
ssh-keygen -f ~/name_key_file_rsa -t rsa -b 2048
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
