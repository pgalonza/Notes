---
title: "Install Arch"
draft: false
---

{{< toc >}}

## Arch install

### Disk layout

```bash
fdisk /dev/sdX
```

Type to clear out any partitions on the drive

o

Type to list partitions. There should be no partitions left.

p

Type to create boot partition

n -> p -> +100M

Type to create root partition

t -> c

Type  to set the first partition to type W95 FAT32 (LBA)

n -> p

Type to write the partition table and exit

w

Create and mount the FAT filesystem

```bash
mkfs.vfat /dev/sdX1
mkdir boot
mount /dev/sdX1 boot
```

Create and mount the ext4 filesystem

```bash
mkfs.ext4 /dev/sdX2
mkdir root
mount /dev/sdX2 root
```

Download and extract the root filesystem (as root, not via sudo):

```bash
wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-2-latest.tar.gz | http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-3-latest.tar.gz
bsdtar -xpf ArchLinuxARM-rpi-2-latest.tar.gz -C root
sync
```

Move boot files to the first partition

```bash
mv root/boot/* boot
```

Unmount the two partitions

```text
bashumount boot root
```

## Tweaks

No space left on device when building packages

_/mnt/root/etc/fstab_

```text
tmpfs   /tmp         tmpfs   rw,nodev,nosuid,size=2G          0  0
```

**sd card class 10**

_/mnt/boot/config.txt_

```text
dtparam=sd_overclock=100
force_turbo=1
boot_delay=1
```

## Initialize

Initialize the pacman keyring and populate the Arch Linux ARM package signing keys

```bash
pacman-key --init
pacman-key --populate archlinuxarm
```

Rootfs use f2fs file system

```bash
pacman -S f2fs-tools
```

Sudo

```bash
pacman -S sudo
```

_/etc/sudoers.d/myOverrides_

```text
alarm  ALL=NOPASSWD: ALL
```

Locale en_US.UTF-8 UTF-8, ru_RU.UTF-8 UTF-8
_/etc/locale.gen_

```bash
locale-gen
```

Add export
_/etc/profile_

```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

Time zone

```bash
ls /usr/share/zoneinfo/
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
date
```

## Desktop
XFCE4

```bash
pacman -S xorg-server xf86-video-fbdev xorg-xrefresh
pacman -S make gcc git automake autoconf pkg-config libtool
pacman -S xfce4 xfce4-goodies xarchiver pavucontrol
```

Display manager

```bash
sudo pacman -S lightdm
```

Greeter

```bash
pacman -S lightdm-gtk-greeter
```

_/etc/lightdm/lightdm.conf_

```bash
greeter-session=lightdm-yourgreeter-greeter
systemctl enable lightdm.service
```

Fonts

```bash
pacman -S ttf-hack ttf-droid ttf-ubuntu-font-family
```

## Install

Yaourt

```bash
pacman -S --needed base-devel git wget yajl
git clone https://aur.archlinux.org/package-query.git
cd package-query
makepkg -si
cd ..
git clone https://aur.archlinux.org/yaourt.git
cd yaourt
makepkg -si
cd ..
```

```bash
yaourt -Syu --devel --aur
```

## BlackArch

Install script

```bash
curl -O https://blackarch.org/strap.sh
```

The SHA1 sum should match: 9f770789df3b7803105e5fbc19212889674cd503 strap.sh

```bash
sha1sum strap.sh
```

Set execute bit

```bash
chmod +x strap.sh
```

Run strap.sh

```bash
./strap.sh
```

To list all of the available tools, run

```bash
pacman -Sgg | grep blackarch | cut -d' ' -f2 | sort -u
```

To install all of the tools, run

```bash
pacman -S blackarch
```

To install a category of tools, run

```bash
pacman -S blackarch-<category>
```

To see the blackarch categories, run

```bash
pacman -Sg | grep blackarch
```
