---
title: "RouterOS"
draft: false
description: "RouterOS notes"
---

{{< toc >}}

IGMP Proxy
Address on interface

Remove all

```bash
remove [find]
```

Show list

```bash
:foreach i in=[/interface vrrp find] do={ :put [/interface vrrp get $i name];
```

Instruction if

```bash
:if ([:len [/file find name=file_name]] > 0) do={:put "false"}
```

Print variable

```bash
:local variable_name [:len [/file find name=name_file]]; :put (variable_name);
```

## IPv6

IPv6 MTU over PPPoE Interface
IPv4 + ICMPv4 = 28
IPv4 + TCP = 40
IPv6 + ICMPv6 = 48
IPv6 + TCP = 60

```text
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn in-interface=6to4 tcp-mss=1221-65535 log-prefix=""
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn out-interface=6to4 tcp-mss=1221-65535 log-prefix=""
```

## NAT

Local network access to an external IP address
_/ip firewall nat_

```text
add action=dst-nat chain=dstnat dst-address=remote_host dst-port=80,443 in-interface-list=LAN protocol=tcp src-address=10.0.192.0/20 to-addresses=local_host
add action=masquerade chain=srcnat dst-address=local_host dst-port=80,443 out-interface-list=LAN protocol=tcp src-address=10.0.192.0/20
```

## Queues

### Hierarchical Token Bucket

Mangle

```text
add action=mark-connection chain=forward new-connection-mark=lan-connection passthrough=yes src-address=local_network
add action=mark-packet chain=forward comment=upload new-packet-mark=upload-packet out-interface=wan passthrough=no
add action=mark-packet chain=forward comment=download new-packet-mark=download-packet out-interface=lan passthrough=no
```

Queue Tree

```text
add name="Global" parent=global
add max-limit=90M name="name" parent=Global
add name=DOWNLOAD parent="name"
add name=UPLOAD parent="name"
add name=download packet-mark=download-packet,download-packet-ipv6 parent=DOWNLOAD queue=pcq-download
add name=upload packet-mark=upload-packet,upload-packet-ipv6 parent=UPLOAD queue=pcq-upload
```

## Security

HoneyPot
_/ip firewall filter_

```text
add action=add-src-to-address-list address-list=block_list address-list-timeout=1d chain=input comment="input stage block" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage1
add action=add-src-to-address-list address-list=block_stage1 address-list-timeout=1m chain=input comment="input stage 1" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage2
add action=add-src-to-address-list address-list=block_stage2 address-list-timeout=1m chain=input comment="input stage 2" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage3
add action=add-src-to-address-list address-list=block_stage3 address-list-timeout=1m chain=input comment="input stage3" connection-state=new dst-address= dst-port= protocol=tcp
```

_/ip firewall raw_

```text
add action=drop chain=prerouting in-interface= log=yes log-prefix=raw_ src-address-list=block_list
```

Port scanners
_/ip firewall filter_

```text
add chain=input protocol=tcp psd=21,3s,3,1 action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="block_list to list " disabled=no
add chain=input protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="NMAP FIN Stealth scan"
add chain=input protocol=tcp tcp-flags=fin,syn action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="SYN/FIN scan"
add chain=input protocol=tcp tcp-flags=syn,rst action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="SYN/RST scan"
add chain=input protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="FIN/PSH/URG scan"
add chain=input protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="ALL/ALL scan"
add chain=input protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="NMAP NULL scan"
```

_/ip firewall raw_

```text
add action=drop chain=prerouting in-interface= log=yes log-prefix=raw_ src-address-list=block_list
```

## VRRP

Master

```text
/interface vrrp add interface=ether1 name=vrrp password=vrrp_password priority=vrrp_priority vrid=vrrp_id
/ip address add address=connection_ip comment=VRRP interface=ether1 network=
/ip address add address=vrrp_ip interface=vrrp network=
```

Slave

```text
/interface vrrp add interface=ether1 name=vrrp password=vrrp_password priority=vrrp_priority vrid=vrrp_id
/ip address add address=connection_ip comment=VRRP interface=ether1 network=
/ip address add address=vrrp_ip interface=vrrp network=
```

## Serial port

Speed = 115200

## backup

```bash
#!/bin/bash

set -x

LOGIN=<user name>
DATE=$(date +%Y-%m-%d_%k-%M-%S)

declare -A devices
devices[<name1>]=<ip address1>
devices[<name2>]=<ip address2>
devicesName=(<name1> <name2>)

function backup() {
  ssh $LOGIN@$1 "/system/backup/save dont-encrypt=yes name=$2-$DATE.backup"
  scp $LOGIN@$1:~/$2-$DATE.backup .
  ssh $LOGIN@$1 "/file remove $2-$DATE.backup"
  ssh $LOGIN@$1 "export terse verbose file=$2-$DATE"
  scp $LOGIN@$1:~/$2-$DATE.rsc .
  ssh $LOGIN@$1 "/file remove $2-$DATE.rsc"
}

for name in ${devicesName[@]}; do
        backup ${devices[$name]} $name
done
```
