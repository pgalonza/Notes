# RouterOS
## PPPoE
IGMP Proxy
Address on interface

## IPv6
IPv6 MTU over PPPoE Interface
```
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn in-interface=6to4 tcp-mss=1221-65535 log-prefix=""
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn out-interface=6to4 tcp-mss=1221-65535 log-prefix=""
```

## NAT
Local network access to an external IP address
_/ip firewall nat_
```
add action=dst-nat chain=dstnat dst-address=remote_host dst-port=80,443 in-interface-list=LAN protocol=tcp src-address=10.0.192.0/20 to-addresses=local_host
add action=masquerade chain=srcnat dst-address=local_host dst-port=80,443 out-interface-list=LAN protocol=tcp src-address=10.0.192.0/20
```

## Queues
### Hierarchical Token Bucket
Mangle
```
add action=mark-connection chain=forward new-connection-mark=lan-connection passthrough=yes src-address=local_network
add action=mark-packet chain=forward comment=upload new-packet-mark=upload-packet out-interface=wan passthrough=no
add action=mark-packet chain=forward comment=download new-packet-mark=download-packet out-interface=lan passthrough=no
```

Queue Tree
```
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
```
add action=add-src-to-address-list address-list=block_list address-list-timeout=1d chain=input comment="input stage block" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage1
add action=add-src-to-address-list address-list=block_stage1 address-list-timeout=1m chain=input comment="input stage 1" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage2
add action=add-src-to-address-list address-list=block_stage2 address-list-timeout=1m chain=input comment="input stage 2" connection-state=new dst-address= dst-port= protocol=tcp src-address-list=block_stage3
add action=add-src-to-address-list address-list=block_stage3 address-list-timeout=1m chain=input comment="input stage3" connection-state=new dst-address= dst-port= protocol=tcp
```

_/ip firewall raw_
```
add action=drop chain=prerouting in-interface= log=yes log-prefix=raw_ src-address-list=block_list
```

Port scanners
_/ip firewall filter_
```
add chain=input protocol=tcp psd=21,3s,3,1 action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="block_list to list " disabled=no
add chain=input protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="NMAP FIN Stealth scan"
add chain=input protocol=tcp tcp-flags=fin,syn action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="SYN/FIN scan"
add chain=input protocol=tcp tcp-flags=syn,rst action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="SYN/RST scan"
add chain=input protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="FIN/PSH/URG scan"
add chain=input protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="ALL/ALL scan"
add chain=input protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="block_list" address-list-timeout=2w comment="NMAP NULL scan"
```

_/ip firewall raw_
```
add action=drop chain=prerouting in-interface= log=yes log-prefix=raw_ src-address-list=block_list
```

## Serial port
Speed = 115200
