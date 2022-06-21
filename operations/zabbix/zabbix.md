# Zabbix

REMOTE COMMANDS
```
EnableRemoteCommands=1
LogRemoteCommands=1
```

Windows CPU utilization in %
```
system.cpu.util[,system,avg1]
system.cpu.util[,system,avg5]
system.cpu.util[,system,avg15]
```

## Zabbix agent

Zabbix user for mysql check
```
GRANT USAGE ON *.* TO 'zabbix'@'%' IDENTIFIED BY <'superpassword'>;
```

Make zabbix agent directory
```
mkdir /var/lib/zabbix
```

## Zabbix database
_/etc/sysctl.conf_
```
echo vm.swappiness = 10 >> /etc/sysctl.conf
```

_/etc/fstab_
```
defaults,noatime,nosuid,noexec,nodev 0 0
```

## Discovery

Descovery rule
```
discovery[{#MACROS_NAME},snmp_oid]
```

Item prototypes
```
snmp_oid.{#MACROS_NAME}
```
