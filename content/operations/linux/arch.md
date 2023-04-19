---
title: "Arch"
draft: false
---

Ignore the package when update
_/etc/pacman.conf_

```text
IgnorePkg=linux
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
