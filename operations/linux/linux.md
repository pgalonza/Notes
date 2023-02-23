# Linux

Thunderbird check all folders

```bash
mail.server.default.check_all_folders_for_new true
```

Hard disk partitions

```bash
/dev/sda1 — boot
/dev/sda2 — root (/)
/dev/sda3 — home
/dev/sda4 — var
/dev/sda5 — tmp
/dev/sda6 — swap
```

Running some program in background

```bash
nohup <program_name> > <program_name>.out 2> <program_name>.err < /dev/null & echo -n "$!" > pid.file &
```

Restore .bashrc, .bash_profile and .bash_logout

```bash
cp /etc/skel/{.bashrc,.bash_profile,.bash_logout} .
```

Shebang indicate an interpreter for execution under UNIX / Linux operating systems

```bash
#!
```

```bash
#!/bin/bash
#!/bin/env bash 
```

Bash profile scripts

* _/etc/profile.d/_

## Linux printers

Connect Linux to a shared printer on Windows!

1. If have driver installer use it
2. Go to the printer Management window and add a new one
3. Connection Protocol choose smb.
4. In the path field, enter the ip/name of the PC or press the find button to find a PC and printer.
5. Select the driver for the printer.
6. Open the printer configuration file
_/etc/cups/printers.conf_

and edit the parameter _DeviceURI_

```text
DeviceURI smb://[username]%40[domain]:[password]@[pass to printer]
```

## SWAP

### Create SWAP

Swap file

```bash
fallocate -l 1G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
```

## Tools

## FSTAB

Do not allow set-user-identifier or set-group-identifier bits to take effect

```text
nosuid
```

Do not allow direct execution of any binaries on the mounted filesystem

```text
noexec
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
```

## Sudoers

Root without asking password

```bash
<user_name> ALL=(ALL) NOPASSWD: ALL
```

## SystemD

### Nspawn

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

### Units

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

## Users and Groups

Restricted Shells

```bash
useadd <user name> –s /bin/rbash
mkdir –p /home/<user name>/bin
cp /bin/ping /home/<user name>/bin
ln –s /bin/ls /home/<user name>/bin
```

## Reset password

### Mount

```bash
sudo mount /dev/<device id> /mnt
chroot /mnt /bin/bash
passwd <user name>
sudo umount -l /mnt
```

## Grub

1. Choose edit in Grub menu

2. Add in linux line

    ```text
    init=/bin/bash
    ```

3. Change ro to rw

4. Remove single, splash and quiet words

## Chroot

```bash
mount /dev/<root> /mnt
mount /dev/<boot> /mnt/boot
mount --bind /dev /mnt/dev
mount --bind /sys /mnt/sys
mount --bind /proc /mnt/proc
chroot /mnt /bin/bash
```

## Security

Yandex recomendations

```text
# Turn on execshield
kernel.exec-shield=1
kernel.randomize_va_space=1
# Enable IP spoofing protection
net.ipv4.conf.all.rp_filter=1
# Disable IP source routing
net.ipv4.conf.all.accept_source_route=0
# Ignoring broadcasts request
net.ipv4.icmp_echo_ignore_broadcasts=1
net.ipv4.icmp_ignore_bogus_error_messages=1
# Make sure spoofed packets get logged
net.ipv4.conf.all.log_martians = 1
```
