---
title: "Install from LiveOS"
draft: false
description: "Linux install instruction via LiveOS"
---

Load with LiveOS

Mount root partiotion

```bash
mkdir /mnt/root
mount /dev/*/root /mnt/root
```

Download ISO image of linux distribution in /mnt/root

Mount the ISO image

```bash
mkdir /mnt/iso
mount /mnt/root/<image name>.iso /mnt/iso
```

Mount IMG image

```bash
mkdir /mnt/img
mount /mnt/iso/*/<image name>.img /mnt/img
```

Copy files of root file system for temporary environment

```bash
cp -rf /mnt/img/* /mnt/root
```

Mount virtual file systems

```bash
mount --rbind /sys /mnt/root/sys
mount --rbind /proc /mnt/root/proc
mount --rbind /dev /mnt/root/dev
```

Enter in chroot

```bash
chroot /mnt/root /bin/bash
```

Install packages, grub

Configure fstab
