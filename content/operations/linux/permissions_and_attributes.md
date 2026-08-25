---
title: "Permissions, flags and attributes"
draft: false
description: "Linux file permissions, special flags (sticky bit), and capabilities management notes, including recovery techniques for broken chmod."
summary: "A practical guide to Linux permission manipulation, from basic chmod to advanced capabilities and systemd integration."
---

Change uid and gid

```bash
usermod -u 2005 foo
groupmod -g 3000 foo

find / -group 2000 -exec chgrp -h foo {} \;
find / -user 1005 -exec chown -h foo {} \;

usermod -g <NEWGID> <LOGIN>
```

Read ttyUSB0

```bash
chmod a+rw /dev/ttyUSB0
```

Cd rom access

```bash
chmod u+s /usr/bin/wodim
```

End-to-end file access without read directory

```bash
chmod 711 <folder name>
```

Sticky Bit

```bash
chmod +t <folder or file name>
```

Restore execute bit to chmod tool

[Information from](https://t.me/loose_code/829)

```bash
setfacl -m u::rwx,g::rx,o::x /usr/bin/chmod
/usr/lib64/ld-linux-x86-64.so.2 /usr/bin/chmod +x /usr/bin/chmod
cp --attributes-only /usr/bin/ls ./new_chmod; cat /usr/bin/chmod > ./new_chmod
install -m 755 /usr/bin/chmod ./new_chmod
rsync --chmod=ugo+x /usr/bin/chmod ./new_chmod
python -c "import os;os.chmod('/usr/bin/chmod', 0755)"
```

Get extended attributes

```bash
getfattr <file name>
```

## Capabilities

[Information from](https://t.me/cybersec_academy/1684)


Get all files with capabilities

```bash
getcap -r /
```

Set capabilities in systemd Unit

```bash
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
AmbientCapabilities=CAP_NET_BIND_SERVICE
```

## ACL

Set default permissions

```bash
setfacl -d -m u::rwx,g::r-x,o::r-x /home/test/
```

Remove default permission

```bash
setfacl -k /home/test/
```

Remove permission

```bash
setfacl -x user_name /home/test/
```

Recursive

```bash
setfacl -R
```

Remove all acl

```bash
setfacl -bn /home/test/
```

View permissions

```bash
getfacl
```

Umask

```bash
umask
```

## Chattr

Make immutable

```bash
chattr +i <file name>
```

Only append

```bash
chattr +a <file name>
```

Kernel compress/decompress

```bash
chattr +c <file name>
```

Ignore when dump

```bash
chattr +d <file name>
```

Security remove

```bash
chattr +s <file name>
```

Remove with save data

```bash
chattr +u <file name>
```

Sync on disk

```bash
chattr +S <file name>
```

Show the file attributes

```bash
lsattr file_name
```
