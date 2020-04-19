# LVM
## Resize LVM
### Add new disk

Connect to disk
```
fdisk /dev/sdX
```

Create the partition
```
: n
```

Type primary
```
: p
```

Type of partition
```
:t : 8e
```

Write changes
```
: w
```

Update info about size
```
partprobe
```

Create the volume
```
pvcreate /dev/sdXX
```

Add to volume group
```
vgdisplay
vgextend volume_group /dev/sdXX
```

Expend the space
```
lvdisplay
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group
```
resize2fs /dev/volume_group/logical_volume
```

### Extend
Resize
```
(parted) resizepart
```

Resize physical volume
```
pvresize /dev/sdX
```

Expend the space
```
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group
```
resize2fs /dev/volume_group/logical_volume
```

## Move partition on new disk

Create similar partitions on a new disk
```
fdisk
parted
```

Copy the boot partition
```
dd if=/dev/sda1 of=/dev/sdb1
```

Create the volume
```
pvcreate /dev/sdbx
```

Add to volume group
```
vgextend volume_group /dev/sdX
```

Move the partition
```
pvmove /dev/sdax /dev/sdbX
```

Remove from volume group
```
vgreduce volume_group-vg /dev/sdXX
```

Remove from lvm
```
premove /dev/sdXX
```

Install the grub2
```
grub-install --target=x86_64-efi /dev/sdX
```

Expend the space
```
lvdisplay
lvextend -l +100%FREE /dev/volume_group/logical_volume
```

Resize the volume group
```
resize2fs /dev/volume_group/logical_volume
```
