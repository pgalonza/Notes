---
title: "SSH"
draft: false
---

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
