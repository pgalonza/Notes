---
title: "Install Arch"
draft: false
---

## Настройка wifi

```bash
wifi-menu
```

## Разметка

Смотрим разделы

```bash
fdisk -l
```

Запускаем утилиту для редактирования разделов и указываем физический диск.
Для UEFI создаем раздел 100M вне LVM в vfat

```bash
cfdisk /dev/sdX
```

```bash
mkfs.fat -F32 /dev/sda1
```

## LVM

Загружаем модуль ядра

```bash
modprobe dm-mod
```

Помещаем заголовок на разделы

```bash
pvcreate /dev/sdaX
```

Выводим разделы для LVM

```bash
pvdisplay
```

Создаем логические тома

```bash
vgcreate "имя_LVM" /dev/sdaX
```

Создание логического раздела

```bash
lvcreate –L "размер" "имя_LVM" –n "имя_раздела"         #обычные разделы
lvcreate –C y –L "размер" "имя_LVM" –n имя_раздела      #swap раздел
lvcreate –l +100%FREE "имя_LVM" –n имя_раздела          #остальное место
```

Отображаем логические тома

```bash
vgdisplay
```

Отображаем логические раздела

```bash
lvdisplay
```

Делаем группы доступными

```bash
vgscan
vgchange –ay
```

## File system

Форматируем обычный раздел

```bash
mkfs.extX /dev/sdaX
```

Форматируем раздел тома

```bash
mkfs.extX /dev/"имя_LVM"/"имя_раздела"
```

Форматируем раздел под SWAP

```bash
mkswap /dev/имя_LVM/"имя_раздела"
```

Монтируем корень

```bash
mount /dev/"имя_LVM"/"имя_раздела" /mnt
```

Создаем директории и монтируем туда разделы

```bash
mkdir -p /mnt/"имя_раздела" && mount /dev/"имя_LVM|раздела" /mnt/"имя_раздела"
```

Монтируем SWAP

```bash
swapon /dev/"имя_LVM"/"имя_раздела"
```

Отображаем смонтированные разделы

```bash
mount | grep \/mnt
```

## Base installation

Выбираем зеркало. Указываем 5-ть зеркал в начале файла.
_/etc/pacman.d/mirrorlist_

Установка системы

```bash
pacstrap /mnt base base-devel
```

Генерируем файл fstab

```bash
genfstab -U -p  /mnt >> /mnt/etc/fstab
```

Отображаем fstab
_/mnt/etc/fstab_

Открываем сеанс в нашей системе

```bash
arch-chroot /mnt
```

Делаем ссылку на временную зону

```bash
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
```

Генерируем файл /etc/adjtime

```bash
hwclock --systohc --utc
```

Устанавливаем имя узла

```bash
echo мое_имя_узла > /etc/hostname
```

Вносим имя узла в hosts
_/etc/hosts_

```bash
#<ip-address>   <hostname.domain.org>   <hostname>
127.0.0.1   localhost.localdomain        localhost
127.0.1.1   мое_имя_узла.localdomain     мое_имя_узла
::1         localhost.localdomain        localhost
```

Устанавливаем пароль для root

```bash
passwd
```

Создаем пользователя

```bash
useradd -m -G wheel "имя_пользоввателя"
```

Задаем для пользователя пароль

```bash
passwd "имя_пользоввателя"
```

Отображаем настройки /etc/sudoers и активируем группу wheel
_/etc/sudoers_

Выбираем локаль en_US.UTF-8, ru_RU.UTF-8
_/etc/locale.gen_

Генерируем локаль

```bash
locale-gen
```

Определяем раскладку клавиатуры

```bash
echo KEYMAP=ru >> /etc/vconsole.conf
```

Отображаем настройки vconsole.conf
_cat /etc/vconsole.conf_

Редактируем хуки для LVM
_/etc/mkinitcpio.conf_

```bash
#HOOKS="base udev autodetect modconf block lvm2 scsi keyboard filesystems fsck shutdown"
```

Генерируем образ initramfs

```bash
mkinitcpio -p linux
```

## Grub

Установка grub

```bash
pacman -S grub || efibootmgr
```

Устанавливаем загрузчик

```bash
grub-install --target=x86_64-efi /dev/sdx
grub-install --recheck /dev/sdx
grub-install --efi-directory=/boot/efi --boot-directory=/boot --bootloader-id=GRUB --target=x86_64-efi --recheck
```

Копипастим что-то важное

```bash
cp /usr/share/locale/en\@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo
```

Для Windows UEFI
_/etc/grub.d/40_custom_

```bash
menuentry 'Windows 10' {
    search --fs-uuid --no-floppy --set=root "UUID"
    chainloader (${root})/EFI/Microsoft/Boot/bootmgfw.efi
}
```

Генерируем конфиг

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

Отображаем
_/boot/grub/grub.cfg_
_/boot/grub/menu.lst_

```text
# (0) Arch Linux
#title  Arch Linux
#root   (hd0,0)
#kernel /vmlinuz26 root=/dev/mapper/VolGroup00-lvolroot resume=/dev/mapper/VolGroup00-lvolswap ro
#initrd /kernel26.img
```

UEFI windows
_/etc/grub/40_customc_

EFI bootloader

```bash
mkdir /boot/efi/EFI/BOOT
cp /boot/efi/EFI/GRUB/grubx64.efi /boot/efi/EFI/BOOT/BOOTX64.EFI
```

File _/boot/efi/startup.nsh_

```bash
bcfg boot add 1 fs0:\EFI\GRUB\grubx64.efi "My GRUB bootloader"
```

## Установка KDE

Устанавливаем x-сервер плазму и консоль

```bash
pacman -S xorg xorg-xinit plasma konsole kate dolphin
```

Устанавливаем тему

File _/etc/sddm.conf_

```text
Current=breeze
```

Ставим на автозапуск sddm

```bash
systemctl enable sddm
```

Устанавливаем dialog для wifi-menu

```bash
pacman -S dialog
```

Устанавливаем менеджер подкючений

```bash
pacman networkmanager
```

Ставим менеджер подключений на автозупуск

```bash
systemctl enable NetworkManager
```

Создаем попку для кэша KDE

```bash
mkdir ~/.compose-cache/
```

Драйвер для видео карты

```bash
pacman -S xf86-video-intel
```

Устанавливаем pikaur

```bash
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/pikaur.git
cd pikaur
makepkg -fsri
```

Ставим остальной софт

Размантируем разделы

```bash
unmount /mnt{имя_раздела,}
```

## Install the AUR helper

Install dependencies

```bash
sudo pacman -S --needed base-devel git
```

Get the source from GitHub

```bash
git clone https://github.com/actionless/pikaur.git
```

Make

```bash
makepkg -fsri
```
