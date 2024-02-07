---
title: Network
draft: false
description: "CLI commands for NetStat"
---

{{< toc >}}

Check MTU

```bash
ping <ip_address> -4 -M do -s $((1500-28))
ping <ip_address> -6 -M do -s $((1500-48))
```

Check port

```bash
(echo > /dev/tcp/<ip>/<port number>) > /dev/null 2>&1 && echo "success"
```

## Network

Forward

```bash
echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf
echo net.ipv6.conf.all.forwarding=1 >> /etc/sysctl.conf
```

IPv6
_/etc/sysconfig/network_

```text
NETWORKING_IPV6=yes
```

IPv6 and IPv4 priority
_/etc/gai.conf_

### VLAN

Adding new virtual interface

```bash
ip link add link ethX name ethX.vlan_id type vlan id vlan_id
```

Assign ip-address to interface

```bash
ip addr add X.X.X.X/XX dev ethX.vlan_id
```

Enabling the interface

```bash
ip link set dev ethX.vlan_id up
```

### MACVLAN

Adding new macvlan interface

```bash
ip link add link ethX macvlan_name type macvlan mode bridge
```

### Bridge

Adding new bridge interface

```bash
ip link add name bridge_name type bridge
```

Adding interface to bridge

```bash
ip link set interface_name master bridge_name
```

Removing interface

```bash
ip link set interface_name nomaster
```

### VRRP


LVS + Keepalived.

```text
global_defs {
    enable_script_security
    router_id <name>
}

vrrp_script <block name> {
    script "<command>"
    interval <interval in seconds>
    weight <value for priority -253..253>
    user nobody
}

vrrp_track_process <block name> {
    process <name of proccess>
    interval <interval in seconds>
    weight <value for priority -253..253>
    quorum <minimum number of processes for success>
    quorum_max <maximum number of processes for success>
}

vrrp_instance <block name> {
    state <MASTER/BACKUP>
    interface <interface name>
    virtual_router_id <id, must be same>
    priority <0-255>
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass <password>
    }
    unicast_peer {
        <ip other vrrp host>
    }
    virtual_ipaddress {
        <virtual ip>/<mask> dev <interface name> label <interface name>:vip
    }

    track_process {
        <block name>
    }

   track_script {
       <block name>
    }

}

virtual_server <virtual ip> <port> {

    delay_loop <check delay per seconds>
    lvs_sched <rr|wrr|lc|wlc|lblc|sh|mh|dh|fo|ovf|lblcr|sed|nq|twos>
    lvs_method <NAT|DR>
    protocol <TCP|UDP|SCTP>

    real_server <backend ip> <port> {
        weight 1
        HTTP_GET {
            url {
                status_code 200
            }
            connect_timeout <connection timeout>
        }
    }

    real_server <backend ip> <port> {
        weight 1
        HTTP_GET {
            url {
                path /
                status_code 200
            }
            connect_timeout <connection timeout>
        }
    }
}
```

## NETSTAT

Show all TCP ports

```bash
netstat -at
```

Show all UDP ports

```bashKDE
netstat -au
```

Show all open sockets with pid and name of process

```bash
netstat -p
```

Shown all listening sockets with pid and name of process

```bash
netstat -ltupn
```

List of connecting host

```bash
netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u
```

## NetworkManager

Network configurations

/etc/NetworkManager/system-connections/

/var/run/NetworkManager/system-connections/
