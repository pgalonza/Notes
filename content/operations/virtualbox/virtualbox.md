---
title: "VirtualBox"
draft: false
description: "VirtualBox notes"
---

{{< toc >}}

Change UUID

```bash
VBoxManage internalcommands sethduuid disk_name.vdi
```

## Troubleshooting

Fix the problems

```bash
/sbin/vboxconfig
modprobe vboxdrv
/sbin/rcvboxdrv setup
```
