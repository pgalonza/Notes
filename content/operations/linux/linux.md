---
title: "Linux"
draft: false
---

{{< toc >}}

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

Set variables from property

```bash
#! /bin/nash

function read_properties {
  grep "${1}" <file_name>.properties|cut -d'=' -f2|tr -d '[:space:]'
}

WORK_DIR="$(dirname "$0")"
cd $WORK_DIR

export <variable_name> = $(read_properties <'parameter_name'>)
```

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

_/etc/sysctl.conf_

```text
vm.swappiness=10
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

## Sudoers

Root without asking password

```bash
<user_name> ALL=(ALL) NOPASSWD: ALL
```

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

## Reset password

### Mount

```bash
sudo mount /dev/<device id> /mnt
chroot /mnt /bin/bash
passwd <user name>
sudo umount -l /mnt
```

CIFS

```text
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

Check CIFS if mount

```bash
#!/bin/sh
RESULT=$(mount -v | grep -i -e 'type smb' -e 'type cifs')
if [ -n "$RESULT" ]; then
  exit
else
  mount -a
fi
```

## Grub

1. Choose edit in Grub menu

2. Add in linux line

    ```text
    init=/bin/bash
    ```

3. Change ro to rw

4. Remove single, splash and quiet words

Generate configyration file

```bash
grub-mkconfig -o /boot/grub2/grub.cfg
```

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

## Locale

Set global

```bash
localectl set-locale <locale variable>=<locale value>
vim /etc/locale.conf
```

Set for user

```bash
export <locale variable>=<locale value>
```

## Limits

Get name and path byte limits

```
getconf -a | grep -i name_max
getconf -a | grep -i path_max
```

## PAM limits configuration

_/etc/security/limits.conf_, _/etc/security/_

```text
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

_/etc/systemd/system.conf_, _/etc/systemd/user.conf_,  _/etc/systemd/<systemd_unit>/override.conf_

```text
DefaultLimitNOFILE=
```

_/lib/systemd/system/<service>_, _/etc/systemd/*_, _/usr/lib/systemd/system/<service>_

```text
LimitNOFILE=
```

_override.conf_

```bash
mkdir /etc/systemd/system/service_name.service.d/
```

```ini
[Service]
LimitNOFILE=100000
```

Show limits

```python
import platform

if 'linux' in platform.system().lower():
    import resource  # Linux only

    limit_nofile = resource.getrlimit(resource.RLIMIT_NOFILE)
    limit_nproc = resource.getrlimit(resource.RLIMIT_NPROC)

    print ('Max number of opened files allowed:', limit_nofile)
    print ('Max number of processes allowed', limit_nproc)

```

## Pipes

Create named pipe

```bash
mkfifo <name of pipe>
mknod <name of pipe> p
```

Write in pipe

```bash
echo <> > <pipe path>
```

Read from pipe

```bash
tail -f <pipe path>
```

Remove named pipe

```bash
unlink <pipe path>
```