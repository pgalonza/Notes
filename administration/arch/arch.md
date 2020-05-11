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
