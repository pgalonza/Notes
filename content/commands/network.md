---
title: "Network"
draft: false
---
Check MTU

```bash
ping <ip_address> -4 -M do -s $((1500-28))
ping <ip_address> -6 -M do -s $((1500-48))
```

## NETSTAT

Show all TCP ports

```bash
netstat -at
```

Show all UDP ports

```bash
netstat -au
```

Show all open sockets with pid and name of process

```bash
netstat -p
```

Shown all listening sockets with pid and name of process

```bash
netstat -ltupn
```

List of connecting host

```bash
netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u
```
