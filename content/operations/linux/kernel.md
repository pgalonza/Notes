---
title: "Kernel"
draft: false
description: "Linux kernel notes"
---

{{< toc >}}

## OOM Killer

[Information from](https://t.me/bashdays/40)

Get OOM score

```bash
cat /proc/<pid>/oom_score
```

Disable

```bash
echo 1 > /proc/sys/vm/panic_on_oom
```

Disable for proccess

```bash
echo -17 > /proc/<pid>/oom_adj
```

Set priority

```bash
echo <+-value> > /proc/<pid>/oom_adj
```

## Limits

### File, socket limits

_/etc/sysctl.conf_

Maximum of objects inotify per user

```text
fs.inotify.max_user_instances=
```

Maximum of watch files and directories per object inotify

```text
fs.inotify.max_user_watches=
```

Maximum of events in queued

```text
fs.inotify.max_queued_events=
```

Maximum of open descriptors

```text
fs.file-max=
```

Maximum queue size of packet

```text
net.core.netdev_max_backlog =
```

Maximum number of open sockets waiting to be connected

```text
net.core.somaxconn =
```

## SysRq

Enable

* On work

    ```bash
    sysctl kernel.sysrq=1
    echo "1" > /proc/sys/kernel/sysrq
    ```

* On boot

    ```bash
    echo "kernel.sysrq = 1" >> /etc/sysctl.d/99-sysctl.conf
    ```

* Before mounting and ini

    _Kernel_

    ```text
    sysrq_always_enabled=1
    ```

Set dump directory

```text
kernel.core_pattern = <path>/core.%u.%e.$p
```

## Make and build

Configure

```bash
make menuconfig
```

Make kernel all targets

```bash
make -j(<NUMBER_OF_CORES> + 1) all
```

Make modules

```bash
make modules_install
```

Make headers

```bash
make headers_install
```

Install kernel

```bash
make install
```

Show memory overcommit

```bash
cat /proc/sys/vm/overcommit_memory
```
