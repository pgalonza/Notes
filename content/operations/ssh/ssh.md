---
title: "SSH"
draft: false
description: "SSH notes"
---

{{< toc >}}

Remove all keys host from known_hosts

ssh-keygen -R <host_name>

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

Connect

```bash
ssh -XYC <user_name>@<host_name>
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
