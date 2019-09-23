# Mariadb
## Backup

Read only
```
grant select,lock tables on database_name.* to 'read-only_user_name'@'%'
```

Lock tables
```
FLUSH TABLES WITH READ LOCK
```

## Optimization

The number of open files
_/etc/security/limits.conf_
```
*         hard    nofile      35000
*         soft    nofile      35000
root      hard    nofile      35000
root      soft    nofile      35000
```

Swappiness
_/etc/sysctl.conf_
```
vm.swappiness=10
```

Mount
_/etc/fstab_
```
defaults,noatime,nosuid,noexec,nodev 0 0
```
