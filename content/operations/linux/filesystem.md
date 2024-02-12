---
title: "Filesystem"
draft: false
---

{{< toc >}}

## Commands

View

```bash
fdisk -l
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT
lsblk -f
findmnt
mount | column -t
```

View attrubutes

```bash
blkid /dev/sda(1)
```

Tell the Linux kernel about the presence and numbering of on-disk partitions, update the specified partitions

```bash
partx -u /dev/sda
```

Inform the OS of partition table changes

```bash
partprobe
```

Re-scan disk

```bash
find /sys -iname 'scan'
echo 1>/sys/class/block/sda/device/rescan
```

* SCSI

```bash
echo "- - -" > /sys/class/scsi_host/hostX/scan
```

Copy Hard Drive

```bash
sfdisk -d /dev/sda | sfdisk /dev/sdb
```

Partition synchronization

```bash
rsync -avzr /var/log/ /mnt/
```

What kind of process working with partition

```bash
lsof | grep '/var/log'
```

Show information of dick

```bash
hdparm -I /dev/sda
```

Show inodes

```bash
df -i
```

Make emty files with size

```bash
dd if=/dev/zero of=output.dat  bs=24M  count=1
dd if=/dev/zero of=output.dat  bs=1M  count=24
truncate -s 10M file.txt
fallocate -l $((10*1024*1024)) file.txt
head -c 10MB /dev/urandom > file.txt
```

Show physical location of file

```bash
filefrag -b512 -v <file>
```

## Du

Show size of directories

```bash
du --max-depth=1 -h directory_name
```

Show total and top

```bash
du -chx | sort -h | tail
du -ckx | sort -n | tail
du -hs * | sort -rh | head -5
du -Sh | sort -rh | head -5
```

Show of files

```bash
du -ah directory_name
```

Show directory size

```bash
du -sh directory_name
```

Show hidden directorys

```bash
du -hs .[^.]*
```

## Dd

Copy partition and Hard Drive

```bash
dd if=/dev/sda1 of=/dev/sdb1
dd if=/dev/sda of=/dev/sdb
```

Burn the image

```bash
sudo dd oflag=direct status=progress if=image.iso of=/dev/sd* bs=1M; sync
```

dd with status

```bash
pv -tpreb /dev/sdb | dd of=~/sdb.img bs=1M
```

Make emty files with size

```bash
dd if=/dev/zero of=output.dat  bs=24M  count=1
dd if=/dev/zero of=output.dat  bs=1M  count=24
```

Copy cd-rom

```bash
dd if=/dev/cdrom of=/opt/cd.iso bs=1M
```

Create image

```bash
dd if=/dev/sdc of=flash.img bs=512
ddrescue /dev/sdc flash.img /tmp/flash.log
dcfldd if=/dev/sda1 hash=md5 of=/media/forensic_disk_image.dd bs=512 noerror
```

Ignore Errors

```bash
dd if=/dev/sdc of=flash.img bs=1M conv=noerror
```

Read file from physical location

```bash
dd if=/dev/<sd*> skip=<start offset> status=none count=8
```

## S.M.A.R.T

View

```bash
smartctl -a /dev/sda
```

File system resize

```bash
resize2fs /dev/sda
```

## Raid

Information

```bash
cat /proc/mdstat
```

Add disk

```bash
mdadm --manage /dev/md_number --add /dev/sda
```

Create the raid with one disk

```bash
mdadm --create --verbose /dev/md_number --level=1 --raid-devices=1 /dev/sda
```

Change number of disks

```bash
mdadm --grow /dev/m_number --raid-devices=2
```

## Check and repair the file system

### e2fsprogs

The defragmentation check ext4 partition

```bash
e4defrag -c /dev/sda
```

Defragmentation ext4 partition

```bash
e4defrag /dev/sda
```

Check the result ⩽0.3% non-contiguous

```bash
fsck -n /dev/sda
```

### Fsck

Check the file system

```bash
fsck -CMn /dev/sda1
```

Force check the file system

```bash
fsck -CMnf /dev/sda1
```

Repair the file system

```bash
fsck -p /dev/sda1
```

Repair superblocks

* View backup superblocks

```bash
mkfs -t ext4 -n /dev/sda1
```

* Recovery

```bash
fsck -b "superblocks" /dev/sda1
```

Find badblocks

```bash
fsck -c /dev/sda1
```

### XFS_check

```bash
Check the partition
xfs_check /dev/sdb1
```

### XFS_repair

Check the partition

```bash
xfs_repair -n /dev/sdb1
```

Repair the file system

```bash
xfs_repair /dev/sdb1
```

Force Log Zeroing

```bash
xfs_repair -L  /dev/sdb1
```

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
