---
title: SystemD
draft: false
description: "CLI commands for systemd"
---

{{< toc >}}

Show problems

```bash
systemctl --failed
```

Get pid

```bash
systemctl status systemd-modules-load
```

## Nspawn

Create container system files

```bash
mount rootfs.img /var/lib/machines/<container name>
```

Start container

```bash
systemctl start systemd-nspawn@<container name>
```

Connect to container

```bash
systemd-run -t -M <container name> /bin/bash
```

Show status

```bash
machinectl status <container name>
```

Start on boot

```bash
machinectl enable <container name>
```

Set quotas

```bash
systemctl set-property systemd-nspawn@<container name> CPUQuota=200%
systemctl set-property systemd-nspawn@<container name> MemoryMax=2G
```

## Units

OOMKiller

```text
OOMScoreAdjust=1000
ExecStartPost=/bin/bash -c "echo <memory>G > /sys/fs/cgroup/memory/system.slice/php-fpm.service/memory.memsw.limit_in_bytes"
ExecStartPost=/bin/bash -c "echo 0 > /sys/fs/cgroup/memory/system.slice/php-fpm.service/memory.swappiness"
MemoryLimit=<memory>G
```

Create unit with wrapper
_/etc/systemd/system/\<service name\>.service_

```text
[Unit]
Description=<description>
After=syslog.target network.target
[Service]
SuccessExitStatus=143
User=<username>
Group=<usergroup>

Type=simple

ExecStart=</path to wrapper>
ExecStop=/bin/kill -15 $MAINPID

[Install]
WantedBy=multi-user.target
```

```bash
#!/bin/bash

JAVA_HOME=<java path>
WORKDIR=<service work dir>
JAVA_OPTIONS="<java options>"
APP_OPTIONS="<application options>"

cd $WORKDIR
eval exec "${JAVA_HOME}/bin/java" $JAVA_OPTIONS -jar <jar file>.jar $APP_OPTIONS
```

Docker

```text
[Unit]
Description=<description>
After=docker.service
Requires=docker.service

[Service]
TimeoutStartSec=0
Restart=always
ExecStartPre=-/usr/bin/docker exec %n stop
ExecStartPre=-/usr/bin/docker rm %n
ExecStartPre=/usr/bin/docker pull <docker image>
ExecStart=/usr/bin/docker run --rm --name %n \
    <docker image>

[Install]
WantedBy=default.target
```

## Journalctl

Unit logs in real time

```bash
journalctl -fu <unit_name>
```

Show problems by pid

```bash
journalctl _PID=
```

Show without less

```bash
journalctl --no-pager
```

## Systemd-analyze

Show load time

```bash
systemd-analyze
```

Show load time in detail

```bash
systemd-analyze blame
```

Write load information in svf file

```bash
systemd-analyze plot > graph.svf
```
