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

## Discovery

Descovery rule
```
discovery[{#MACROS_NAME},snmp_oid]
```

Item prototypes
```
snmp_oid.{#MACROS_NAME}
```
