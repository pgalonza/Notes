---
title: "Consul"
date: 2023-08-12T01:08:08+03:00
draft: false
description: "Consul notes"
---

Add forward dns port

```bash
iptables -t nat -I OUTPUT -p tcp -o lo --dport 53 -j REDIRECT --to-ports 8600
iptables -t nat -I OUTPUT -p udp -o lo --dport 53 -j REDIRECT --to-ports 8600
```
