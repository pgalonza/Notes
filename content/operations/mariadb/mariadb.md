---
title: "Mariadb"
draft: false
---

## Backup

Read only

```sql
grant select,lock tables on database_name.* to 'read-only_user_name'@'%'
```

Lock tables

```sql
FLUSH TABLES WITH READ LOCK
```

## Optimization

The number of open files
_/etc/security/limits.conf_

```text
*         hard    nofile      35000
*         soft    nofile      35000
root      hard    nofile      35000
root      soft    nofile      35000
```

Swappiness
_/etc/sysctl.conf_

```text
vm.swappiness=10
```

Mount
_/etc/fstab_

```text
defaults,noatime,nosuid,noexec,nodev 0 0
```

Innodb file format
_/etc/mysql/my.cnf_

```text
innodb_file_format=Barracuda
```

```sql
SET GLOBAL innodb_file_format=BARRACUDA
```

## Troubleshooting

How to fix error “1812 Tablespace is missing for table XXXX”

1. Backup all .ibd and .frm files.
2. Create the database and tables structure.
3. DISCARD the new tables.

    ```sql
    ALTER TABLE table_name DISCARD TABLESPACE;
    ```

4. After that copy the .ibd,.frm files from backup to the database folder.
5. Then IMPORT new files

    ```sql
    ALTER TABLE table_name IMPORT TABLESPACE;
    ```

Can't lock aria control file '/var/lib/mysql/aria_log_control'
_/var/lib/mysql_

```text
rm aria_log*
```
