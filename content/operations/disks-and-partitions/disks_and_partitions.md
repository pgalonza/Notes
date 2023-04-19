---
title: "Disks and partitions"
draft: false
---

## Resize portition

### Extend

Connect to disk

```bash
fdisk /dev/sdX
```

Delete the portition

```text
:d
```

Create the partition

```text
: n
```

Type primary

```text
: p
```

First sector

```text
enter
```

Last sector

```text
enter
```

Type of partition

```text
:t : XX
```

Write changes

```text
: w
```

Update the specified partitions

```bash
partx -u /dev/sdX
```

## Tmpfs

Directory in ram
_/etc/fstab_

```text
tmpfs   path_to_directory        tmpfs   noatime,nodev,nosuid,size=2G          0  0
```

## Check health

Badblocks

```bash
badblocks -v /dev/sdXX -o ~/bad_sectors.txt
badblocks -vn /dev/sdXX -o ~/bad_sectors.txt
```

Ignore badblocks

```bash
e2fsck -l badblocks.txt /dev/sdXX
fsck -l badblocks.txt /dev/sdXX
```

SMART

```bash
smartctl -a /dev/sdXX
```

## Restore

### USB-flash

Create dump

```bash
dd if=/dev/sdc of=flash.img bs=512
ddrescue /dev/sdc flash.img /tmp/flash.log
```

Backup and restore image

```bash
ddrescue flash.img backup_part.img bs=10M count=1
ddrescue backup_part.img flash.img conv=notrunc
```

Recovery data

```bash
testdisk flash.img
photorec flash.img
```
