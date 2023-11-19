---
title: "Molecule"
draft: false
description: "Molecule information"
---

{{< toc >}}

## Systemd in docker

RedHat based

```yaml
  - name: <>
    image: <>
    privileged: true
    cgroupns_mode: host
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    command: /usr/sbin/init
```

Debian based

```yaml
  - name: <>
    image: <>
    privileged: true
    cgroupns_mode: host
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:rw
    command: /sbin/init
```