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
