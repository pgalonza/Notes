---
title: "Security"
date: 2024-08-21T11:52:02+03:00
draft: false
description: "Discover essential security tips and best practices for Linux, designed to protect your server against threats and ensure its smooth operation."
---


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

Search world writw files and dirs

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