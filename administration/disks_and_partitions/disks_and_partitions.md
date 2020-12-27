# Disks and partitions
## Resize portition
### Extend

Connect to disk
```
fdisk /dev/sdX
```

Delete the portition
```
:d
```

Create the partition
```
: n
```

Type primary
```
: p
```

First sector
```
enter
```

Last sector
```
enter
```

Type of partition
```
:t : XX
```

Write changes
```
: w
```

Update the specified partitions
```
partx -u /dev/sdX
```

## Tmpfs

Directory in ram
_/etc/fstab_
```
tmpfs   path_to_directory        tmpfs   noatime,nodev,nosuid,size=2G          0  0
```

## Check health

Badblocks
```
badblocks -v /dev/sdXX -o ~/bad_sectors.txt
badblocks -vn /dev/sdXX -o ~/bad_sectors.txt
```

Ignore badblocks
```
e2fsck -l badblocks.txt /dev/sdXX
fsck -l badblocks.txt /dev/sdXX
```

SMART
```
smartctl -a /dev/sdXX
```

## Restore

### USB-flash

Create dump
```
dd if=/dev/sdc of=flash.img bs=512
ddrescue /dev/sdc flash.img /tmp/flash.log
```

Backup and restore image
```
ddrescue flash.img backup_part.img bs=10M count=1
ddrescue backup_part.img flash.img conv=notrunc
```

Recovery data
```
testdisk flash.img
photorec flash.img
```
