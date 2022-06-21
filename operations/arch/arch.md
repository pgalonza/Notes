# Arch
Ignore the package when update
_/etc/pacman.conf_
```
IgnorePkg=linux
```

## Recovery
### Downgrade package
```
sudo pacman -U /var/cache/pacman/pkg/*.pkg
```

### Downgrade all packages to a specific date
Edit the mirror list
_/etc/pacman.d/mirrorlist_
```
Server = https://archive.archlinux.org/repos/2019/12/02/$repo/os/$arch
```

Downgrade
```
sudo pacman -Syyuu
```

## AUR
### Create packages for AUR from deb
Create _PKGBUILD_ file
```
# Maintainer: maintainer_name
pkgname=package_name
pkgver=package_version
pkgrel=package_release
arch=('i686' 'x86_64')
depends=('package_depends')
license=('package_license')
url="official_site"
pkgdesc="package_description"
source_i686=(url_to_deb)
source_x86_64=(url_to_deb)
sha256sums_i686=('sha256sum')
sha256sums_x86_64=('sha256sum')

package() {
    cd "${pkgdir}"
    tar xf "${srcdir}/data.tar.xz"
}
```

Create _.SRCINFO_ file
```
makepkg --printsrcinfo > .SRCINFO
```

Build package
```
makepkg
```
