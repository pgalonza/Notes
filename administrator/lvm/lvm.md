# Resize LVM

###### Extend

Connect to disk
```
fdisk /dev/sda
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
pvcreate /dev/sda3
```

Add to volume group
```
vgdisplay
vgextend vg_centos /dev/sda3
```

Expend the space
```
lvdisplay
lvextend -l +100%FREE /dev/vg_centos/lv_root
```

Resize the volume group
```
resize2fs /dev/vg_centos/lv_root
```
