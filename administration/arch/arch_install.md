# Arch install
## Настройка wifi
```
wifi-menu
```

## Разметка
Смотрим разделы
```
fdisk -l
```

Запускаем утилиту для редактирования разделов и указываем физический диск.
Для UEFI создаем раздел 100M вне LVM в vfat
```
cfdisk /dev/sdX
```
```
mkfs.fat -F32 /dev/sda1
```

## LVM

Загружаем модуль ядра
```
modprobe dm-mod
```

Помещаем заголовок на разделы
```
pvcreate /dev/sdaX
```

Выводим разделы для LVM
```
pvdisplay
```

Создаем логические тома
```
vgcreate "имя_LVM" /dev/sdaX
```

Создание логического раздела
```
lvcreate –L "размер" "имя_LVM" –n "имя_раздела"         #обычные разделы
lvcreate –C y –L "размер" "имя_LVM" –n имя_раздела      #swap раздел
lvcreate –l +100%FREE "имя_LVM" –n имя_раздела          #остальное место
```

Отображаем логические тома
```
vgdisplay
```

Отображаем логические раздела
```
lvdisplay
```

Делаем группы доступными
```
vgscan
vgchange –ay
```

## File system
Форматируем обычный раздел
```
mkfs.extX /dev/sdaX
```

Форматируем раздел тома
```
mkfs.extX /dev/"имя_LVM"/"имя_раздела"
```

Форматируем раздел под SWAP
```
mkswap /dev/имя_LVM/"имя_раздела"
```

Монтируем корень
```
mount /dev/"имя_LVM"/"имя_раздела" /mnt
```

Создаем директории и монтируем туда разделы
```
mkdir -p /mnt/"имя_раздела" && mount /dev/"имя_LVM|раздела" /mnt/"имя_раздела"
```

Монтируем SWAP
```
swapon /dev/"имя_LVM"/"имя_раздела"
```

Отображаем смонтированные разделы
```
mount | grep \/mnt
```

## Base installation
Выбираем зеркало. Указываем 5-ть зеркал в начале файла.

_/etc/pacman.d/mirrorlist_


Установка системы
```
pacstrap /mnt base base-devel
```

Генерируем файл fstab
```
genfstab -U -p  /mnt >> /mnt/etc/fstab
```

Отображаем fstab

_/mnt/etc/fstab_


Открываем сеанс в нашей системе
```
arch-chroot /mnt
```

Делаем ссылку на временную зону
```
ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime
```

Генерируем файл /etc/adjtime
```
hwclock --systohc --utc
```

Устанавливаем имя узла
```
echo мое_имя_узла > /etc/hostname
```

Вносим имя узла в hosts
_/etc/hosts_
```
#<ip-address>	<hostname.domain.org>	      <hostname>
127.0.0.1	localhost.localdomain	      localhost
127.0.1.1       мое_имя_узла.localdomain      мое_имя_узла
::1		localhost.localdomain	      localhost
```

Устанавливаем пароль для root
```
passwd
```

Создаем пользователя
```
useradd -m -G wheel "имя_пользоввателя"
```

Задаем для пользователя пароль
```
passwd "имя_пользоввателя"
```

Отображаем настройки /etc/sudoers и активируем группу wheel
_/etc/sudoers_


Выбираем локаль en_US.UTF-8, ru_RU.UTF-8
_/etc/locale.gen_


Генерируем локаль
```
locale-gen
```

Определяем раскладку клавиатуры
```
echo KEYMAP=ru >> /etc/vconsole.conf
```

Отображаем настройки vconsole.conf
_cat /etc/vconsole.conf_


Редактируем хуки для LVM
_/etc/mkinitcpio.conf_
```
#HOOKS="base udev autodetect modconf block lvm2 scsi keyboard filesystems fsck shutdown"
```

Генерируем образ initramfs
```
mkinitcpio -p linux
```

## Grub
Установка grub
```
pacman -S grub || efibootmgr
```

Устанавливаем загрузчик
```
grub-install --target=x86_64-efi /dev/sdx
grub-install --recheck /dev/sdx
grub-install --efi-directory=/boot/efi --boot-directory=/boot/efi/EFI --bootloader-id=grub --target=x86_64-efi --removable --recheck
```

Копипастим что-то важное
```
cp /usr/share/locale/en\@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo
```

Для Windows UEFI
_/etc/grub.d/40_custom_
```
menuentry 'Windows 10' {
    search --fs-uuid --no-floppy --set=root "UUID"
    chainloader (${root})/EFI/Microsoft/Boot/bootmgfw.efi
}
```

Генерируем конфиг
```
grub-mkconfig -o /boot/grub/grub.cfg
```

Отображаем
_/boot/grub/grub.cfg_
_/boot/grub/menu.lst_
```
# (0) Arch Linux
#title  Arch Linux
#root   (hd0,0)
#kernel /vmlinuz26 root=/dev/mapper/VolGroup00-lvolroot resume=/dev/mapper/VolGroup00-lvolswap ro
#initrd /kernel26.img
```

UEFI windows
_/etc/grub/40_customc_

EFI bootloader
```
mkdir /boot/efi/EFI/BOOT
cp /boot/efi/EFI/GRUB/grubx64.efi /boot/efi/EFI/BOOT/BOOTX64.EFI
```

_/boot/efi/startup.nsh_
```
bcfg boot add 1 fs0:\EFI\GRUB\grubx64.efi "My GRUB bootloader"
```

# Установка KDE

Устанавливаем x-сервер плазму и консоль
```
pacman -S xorg xorg-xinit plasma konsole kate dolphin
```

Устанавливаем тему

_/etc/sddm.conf_

```
Current=breeze
```

Ставим на автозапуск sddm
```
systemctl enable sddm
```

Устанавливаем dialog для wifi-menu
```
pacman -S dialog
```

Устанавливаем менеджер подкючений
```
pacman networkmanager
```

Ставим менеджер подключений на автозупуск
```
systemctl enable NetworkManager
```

Создаем попку для кэша KDE
```
mkdir ~/.compose-cache/
```

Драйвер для видео карты
```
pacman -S xf86-video-intel
```

Устанавливаем pikaur
```
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/pikaur.git
cd pikaur
makepkg -fsri
```

Ставим остальной софт

Размантируем разделы
```
unmount /mnt{имя_раздела,}
```

## Install the AUR helper
Install dependencies
```
sudo pacman -S --needed base-devel git
```

Get the source from GitHub
```
git clone https://github.com/actionless/pikaur.git
```

Make
```
makepkg -fsri
```
