# Disks and partitions
## Resize portition
### Extend

Connect to disk
```
fdisk /dev/sda
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
partx -u /dev/sda
```

## Tmpfs
Directory in ram
_/etc/fstab_
```
tmpfs   path_to_directory        tmpfs   nodev,nosuid,size=2G          0  0
```
