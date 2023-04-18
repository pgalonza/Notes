---
title: "Zabbix"
draft: false
---

REMOTE COMMANDS

```text
EnableRemoteCommands=1
LogRemoteCommands=1
```

Windows CPU utilization in %

```text
system.cpu.util[,system,avg1]
system.cpu.util[,system,avg5]
system.cpu.util[,system,avg15]
```

## Zabbix agent

Zabbix user for mysql check

```sql
GRANT USAGE ON *.* TO 'zabbix'@'%' IDENTIFIED BY <'superpassword'>;
```

Make zabbix agent directory

```bash
mkdir /var/lib/zabbix
```

## Zabbix database

_/etc/sysctl.conf_

```bash
echo vm.swappiness = 10 >> /etc/sysctl.conf
```

_/etc/fstab_

```text
defaults,noatime,nosuid,noexec,nodev 0 0
```

## Discovery

Descovery rule

```text
discovery[{#MACROS_NAME},snmp_oid]
```

Item prototypes

```text
snmp_oid.{#MACROS_NAME}
```

## Windows counters

Path in the registry

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib\009
```

Get the value

```cmd
typeperf -q ""
```

Re-creating counters

```cmd
lodctr /r
```