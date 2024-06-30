---
title: "Prometheus"
draft: false
description: "Prometheus notes"
---

CPU IOWAIT

```text
irate(node_cpu_seconds_total{mode="iowait"}[5m])
```

CPU LOAD

```text
100 - avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) without(cpu) * 100
```

Free filesystem space

```text
(node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100
```

Incoming bandwidth

```text
sum ithout (device) (rate(node_network_receive_bytes_total{device!="lo"}[30s])) * 8
```
