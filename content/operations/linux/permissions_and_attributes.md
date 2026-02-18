---
title: "Permissions, flags and attributes"
draft: false
description: "Linux permission notes"
---

Change uid and gid

```bash
usermod -u 2005 foo
groupmod -g 3000 foo

find / -group 2000 -exec chgrp -h foo {} \;
find / -user 1005 -exec chown -h foo {} \;

usermod -g <NEWGID> <LOGIN>
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
