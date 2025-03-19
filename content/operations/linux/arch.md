---
title: "Arch"
draft: false
description: "ArchLinux manual"
---

{{< toc >}}

Ignore the package when update
_/etc/pacman.conf_

```text
IgnorePkg=linux
```

Clean cache

```bash
paccache -rk<count of recent versions to keep>
paccache -rk<count of recent versions to keep> --cachedir ~/.cache/pikaur/pkg
paccache -rk<count of recent versions to keep> --cachedir ~/.cache/yay/*/
paccache -rk<count of recent versions to keep> --cachedir /var/cache/private/pikaur/pkg
paccache -ruk0
paccache -ruk0 --cachedir ~/.cache/pikaur/pkg
paccache -ruk0 --cachedir ~/.cache/yay/*/
paccache -ruk0 --cachedir /var/cache/private/pikaur/pkg
pacman -Sc
yay -Sc
pikaur -Sc
rm -rf /var/cache/private/pikaur/build
```

## Recovery

### Downgrade package

```bash
sudo pacman -U /var/cache/pacman/pkg/*.pkg
```

### Downgrade all packages to a specific date

Edit the mirror list
_/etc/pacman.d/mirrorlist_

```text
Server = https://archive.archlinux.org/repos/2019/12/02/$repo/os/$arch
```

Downgrade

```text
sudo pacman -Syyuu
```

## AUR

### Pikaur

No diff and no edit
*/root/.config/pikaur.conf*

```ini
donteditbydefault = yes
nodiff = yes
```

### Create packages for AUR from deb

Create _PKGBUILD_ file

```text
# Maintainer: maintainer_name

pkgname=package_name
pkgver=package_version
pkgrel=package_release
pkgdesc="package_description"

categories=("<category name>")
arch=('i686' 'x86_64')
depends=('package_depends')
license=('package_license')
url="official_site"
source_i686=(url_to_deb)
source_x86_64=(url_to_deb)
sha256sums_i686=('sha256sum')
sha256sums_x86_64=('sha256sum')

install=<file name>.install

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.xz"
}
```

Create _.install_

```text
post_install() {
    <path to file>
}

```

Create _.SRCINFO_ file

```bash
makepkg --printsrcinfo > .SRCINFO
```

Build package

```bash
makepkg
```

## Wayland

Activation for Plasma

```bash
sudo pikaur -S egl-wayland
echo options nvidia_drm modeset=1 | sudo tee /etc/modprobe.d/nvidia_drm.conf
echo options nvidia_drm fbdev=1 | sudo tee /etc/modprobe.d/nvidia_drm.conf
sudo mkinitcpio -v
```

Fix keyboard loyaut in Gnome

_~/.config/fcitx5/conf/wayland.conf_

```text
Allow Overriding System XKB Settings=False
```
