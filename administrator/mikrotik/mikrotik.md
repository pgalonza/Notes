# PPPoE
###### IGMP Proxy
Address on interface

# IPv6

###### IPv6 MTU over PPPoE Interface
```
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn in-interface=6to4 tcp-mss=1221-65535 log-prefix=""
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn out-interface=6to4 tcp-mss=1221-65535 log-prefix=""
```

# NAT
###### Local network access to an external IP address
```
/ip firewall nat
```
```
add action=dst-nat chain=dstnat dst-address=remote_host dst-port=80,443 in-interface-list=LAN protocol=tcp src-address=10.0.192.0/20 to-addresses=local_host
add action=masquerade chain=srcnat dst-address=local_host dst-port=80,443 out-interface-list=LAN protocol=tcp src-address=10.0.192.0/20
```

# Queues
## Hierarchical Token Bucket
###### Mangle
```
add action=mark-connection chain=forward new-connection-mark=lan-connection passthrough=yes src-address=local_network
add action=mark-packet chain=forward comment=upload new-packet-mark=upload-packet out-interface=wan passthrough=no
add action=mark-packet chain=forward comment=download new-packet-mark=download-packet out-interface=lan passthrough=no
```

###### Queue Tree
```
add name=Global parent=global
add max-limit=90M name="name" parent=Global
add name=DOWNLOAD parent="name"
add name=UPLOAD parent="name"
add name=download packet-mark=download-packet,download-packet-ipv6 parent=DOWNLOAD queue=pcq-download
add name=upload packet-mark=upload-packet,upload-packet-ipv6 parent=UPLOAD queue=pcq-upload
```
