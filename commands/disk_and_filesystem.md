# Disks and partitions

###### View
```
fdisk -l
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT
lsblk -f
```

###### Tell the Linux kernel about the presence and numbering of on-disk partitions, update the specified partitions
```
partx -u /dev/sda
```

###### Inform the OS of partition table changes
```
partprobe
```

###### Re-scan disk
```
find /sys -iname 'scan'
echo 1>/sys/class/block/sda/device/rescan
```

SCSI
```
echo "- - -" > /sys/class/scsi_host/hostX/scan
```

###### Copy partition
```
dd if=/dev/sda of=/dev/sdb
```

###### Copy partition table
MBR
```
sfdisk -d /dev/sda | sfdisk /dev/sdb
```

GPT sda to sdb
```
sgdisk -R=/dev/sdb /dev/sda
```

###### Formatting
```
mkfs.ext4 /dev/sda
```

###### Partition synchronization
```
rsync -avzr /var/log/ /mnt/
```

###### What kind of process working with partition
```
lsof | grep '/var/log'
```

# S.M.A.R.T

###### View
```
smartctl -a /dev/sda
```

###### File system resize
```
resize2fs /dev/sda
```

# Raid

###### Information
```
cat /proc/mdstat
```

###### Add disk
```
mdadm --manage /dev/md_number --add /dev/sda
```

###### Create the raid with one disk
```
mdadm --create --verbose /dev/md_number --level=1 --raid-devices=1 /dev/sda
```

###### Change number of disks
```
mdadm --grow /dev/m_number --raid-devices=2
```

# Check and repair the file system
## e2fsprogs
###### The defragmentation check ext4 partition
```
e4defrag -c /dev/sda
```
###### Defragmentation ext4 partition
```
e4defrag /dev/sda
```

###### Check the result ⩽0.3% non-contiguous
```
fsck -n /dev/sda
```

## Fsck
###### Check the file system
```
fsck -CMn /dev/sda1
```

###### Force check the file system
```
fsck -CMnf /dev/sda1
```

###### Repair the file system
```
fsck -p /dev/sda1
```

###### Repair superblocks
View backup superblocks
```
mkfs -t ext4 -n /dev/sda1
```

Recovery
```
fsck -b "superblocks" /dev/sda1
```

###### Find badblocks
```
fsck -c /dev/sda1
```
