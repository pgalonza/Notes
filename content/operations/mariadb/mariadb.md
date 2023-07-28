---
title: "Mariadb"
draft: false
---

{{< toc >}}

## Commands

Initializes the data directory

```bash
mysql_install_db
mariadb-install-db
```

Set security settings

```bash
mysql_secure_installation
mariadb-secure-installation
```

Check & Repair

```bash
mysqlcheck --check-upgrade --all-databases --auto-repair
mysql_upgrade --force
```

Clear command history

```bash
rm $HOME/.mysql_history
```

Export dump

```bash
mysqldump  --skip-extended-insert my_db | gzip > DUMP_FILE.sql.gz
```

Import dump

```bash
gunzip < DUMP_FILE.sql.gz | mysql my_db --user= --password= --host=
```

Monitor the database

```bash
mytop --prompt -d database_name
```

## SQL

Create database

```bash
echo "CREATE DATABASE `my_db` CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql
```

Create user

```bash
echo "CREATE USER 'name'@'localhost' IDENTIFIED BY 'password';" | mysql
```

Give privileges for user

```bash
echo "GRANT ALL PRIVILEGES ON `db`.* TO 'name'@'localhost';" | mysql
```

Reloads the privileges

```bash
echo "FLUSH PRIVILEGES;" | mysql
```

Edit user account

```bash
echo "RENAME USER 'name'@'localhost' TO 'name'@'%';" | mysql
```

Last entry

```bash
SELECT MAX(`my_table`) FROM my_db;
SELECT TOP 10 * FROM my_db ORDER BY my_table DESC
```

Set password for user

```bash
echo "ALTER USER 'name'@'localhost' IDENTIFIED BY 'MyNewPass';" | mysql
```

Delete user

```bash
echo "DROP USER 'name'@'localhost';" | mysql
```

User as root privileges

```bash
echo "GRANT ALL PRIVILEGES ON *.* TO 'name'@'%' with GRANT OPTION;" | mysql
```

Give backup privileges for user

```bash
echo "GRANT SELECT, SHOW VIEW, EVENT, TRIGGER, RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'name'@'localhost'" | mysql
```

```bash
USE database_name;
SOURCE path_to_sql_file;
```

InnoDB warnings become errors instead

```bash
SET GLOBAL innodb_strict_mode=ON;
SET SESSION innodb_strict_mode=ON;
```

Check foreign key constraints for InnoDB tables

```bash
SET FOREIGN_KEY_CHECKS = 1
```

Show in which table the column

```bash
SELECT *
FROM information_schema.columns
WHERE column_name='column_name';
```

Show information about table

```bash
DESCRIBE table_name;
```

Show query information

```bash
EXPLAIN SELECT * FROM categories
```

Count rows in table

```bash
SELECT COUNT(*) FROM table_name
```

## Backup

Read only

```sql
grant select,lock tables on database_name.* to 'read-only_user_name'@'%'
```

Lock tables

```sql
FLUSH TABLES WITH READ LOCK
```

Backup tools

```bash
mysqldump -u${USER} -p${PASSWORD} --skip-extended-insert <database> | gzip > ${DIR}/<database>${NAME}.sql.gz
mariabackup --backup --target-dir=${DIR}/${NAME} --user=${USER} --password=${PASSWORD}
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

## Configuration

Client

```ini
[client]
default-character-set = utf8
user = 
password = 

[mysqladmin]
default-character-set = utf8
user = 
password = 
```

Server

```ini
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
init-connect="SET NAMES utf8"

skip-name-resolve       = 1
server-id=mMariadb1

log_error               = /var/log/mysql/mysql_error.log
log_bin                 = /var/log/mysql/mysql_bin.log
expire_logs_days        = 7
max_binlog_size         = 1G

innodb_file_per_table   = 1
innodb_buffer_pool_size = 500M
innodb_log_file_size    = 16M
innodb_flush_log_at_trx_commit = 1
innodb_flush_method     = O_DIRECT
max_connections         = 160

wait_timeout            = 32400
interactive_timeout     = 32400
max_allowed_packet      = 8M
connect_timeout         = 30

query_cache_size        = 0
query_cache_type        = 0
query_cache_limit       = 5M
join_buffer_size        = 5M
table_open_cache        = 4096

performance_schema      = 1
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
