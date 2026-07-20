---
title: "Security"
date: 2024-08-21T11:52:02+03:00
draft: false
description: "Discover essential security tips and best practices for Linux, designed to protect your server against threats and ensure its smooth operation."
summary: "A collection of Linux security auditing commands to detect misconfigurations, exposed secrets, suspicious files, and unauthorized access for hardening your system."
---

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

### PAM limits configuration

_/etc/security/limits.conf_, _/etc/security/_

```text
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```


## Сollecting information

Search files with secrets

```bash
find . -type f -exec grep -i -I -E "password|secret\w?" {} /dev/null \;
```


Search user with empy password

```bash
awk -F: '($2 == "") {print}' /etc/shadow
```

Search users with uid=0

```bash
awk -F: '($3 == "0") {print}' /etc/passwd
```


Search SUID and SGID

```bash
find / -perm /4000 -or -perm /2000 -print 2> /dev/null
```

Search world writable files and dirs

```bash
find / -xdev -type f \( -perm -0002 -a ! -perm -1000 \) -print
find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print
```

Search files without owner

```bash
 find / -xdev -type f \( -nouser -o -nogroup \) -print
```

Show mounts

```bash
cat /proc/mounts
```

Search crontab

```bash
cat /etc/crontab
```

Search changed files of user

```bash
find . -type f -atime -7 -printf “%AY%Am%Ad%AH%AM%AS %h/%s/%f\n” -user <username>|sort -n
find . -type f -mtime -7 -printf “%TY%Tm%Td%TH%TM%TS %h — %s — %f\n” -user <username>|sort -n
find . -type f -ctime -7 -printf “%CY%Cm%Cd%CH%CM%CS %h — %s — %f\n” -user <username>|sort –n
```

Search for accesses to executable files

```bash
find . -type f -perm /111 -user thole -atime -7 -printf “%AY%Am%Ad%AH%AM%AS %h — %s — %f\n” -user <username>| sort -n
```

Show ports and connections

```bash
ss -tupn
ss -tupnl
```

Verify packages

```bash
dpkg --verify
rpm -Va
dnf check
```

Get processes

```bash
ps auxeww
```

## HASH

Take sum sha1

```bash
echo -n "actual_password_here" | sha1sum | tr [:lower:] [:upper:]
```

Take sum like shadow

```bash
python3 -c "import crypt; print(crypt.crypt('actual_password_here', '\$6\$random_salt\$'))"
```

## FAIL2BAN

View

```bash
fail2ban-client status
fail2ban-client status asterisk-udp
```

Unban

```bash
fail2ban-client set asterisk-udp unbanip ip_address
```

## IPTABLES

View

```bash
iptables -n -L -v --line-numbers
```

## GPG

Import key

```bash
gpg --keyserver keys.gnupg.net --recv-keys key
```

Generate key pair

```bash
gpg --full-gen-key
```

Show private keys

```bash
gpg --list-secret-keys --keyid-format LONG <email>
```

Export public key

```bash
gpg --armor --export <key_id>
```

## Keyring

Get key

```bash
keyring get <service name> <username>
```

## Secret tool

Get key

```bash
secret-tool lookup <attribute> <value>
```