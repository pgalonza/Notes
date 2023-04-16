---
title: "LVM"
draft: false
---

## Resize LVM

### Add new disk

Connect to disk

```bash
fdisk /dev/sdX
```

Create the partition

```text
: n
```

Type primary

```text
: p
```

Type of partition

```text
:t : 8e
```

Write changes

```text
: w
```

Update info about size

```bash
partprobe
```

Create the volume

```bash
pvcreate /dev/sdXX
```

Add to volume group

```bash
vgdisplay
vgextend volume_group /dev/sdXX
```

Expend the space

```bash
lvdisplay
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group

```bash
resize2fs /dev/volume_group/logical_volume
```

### Extend

Resize

```text
(parted) resizepart
```

Resize physical volume

```bash
pvresize /dev/sdX
```

Expend the space

```bash
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group

```bash
resize2fs /dev/volume_group/logical_volume
```

## Move partition on new disk

Create similar partitions on a new disk

```bash
fdisk
parted
```

Copy the boot partition

```bash
dd if=/dev/sdX1 of=/dev/sdX1
```

Create the volume

```bash
pvcreate /dev/sdbx
```

Add to volume group

```bash
vgextend volume_group /dev/sdX
```

Move the partition

```bash
pvmove /dev/sdax /dev/sdbX
```

Remove from volume group

```bash
vgreduce volume_group-vg /dev/sdXX
```

Remove from lvm

```bash
premove /dev/sdXX
```

Install the grub2

```bash
grub-install --target=x86_64-efi /dev/sdX
```

Expend the space

```bash
lvdisplay
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group

```bash
resize2fs /dev/volume_group/logical_volume
```
