---
title: "Consul"
date: 2023-08-12T01:08:08+03:00
draft: false
description: "Consul notes"
---

Add forward dns port iptables

```bash
iptables -t nat -I OUTPUT -p tcp -o lo --dport 53 -j REDIRECT --to-ports 8600
iptables -t nat -I OUTPUT -p udp -o lo --dport 53 -j REDIRECT --to-ports 8600
```

Add forward firewalld

```bash
firewall-cmd  --permanent --direct --add-rule ipv4 nat OUTPUT 0 -p tcp -o lo --dport 53 -j REDIRECT --to-ports 8600
firewall-cmd  --permanent --direct --add-rule ipv4 nat OUTPUT 0 -p udp -o lo --dport 53 -j REDIRECT --to-ports 8600
```
