---
title: "Database"
draft: false
---

## MySQL/MariaDB

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

## PostgreSQL

Login as a postgres user

```bash
su - postgres
sudo -u postgres psql
```

Connenct to console

```bash
psql
```

Exit

```bash
\q
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

Import dump

```bash
gunzip < DUMP_FILE.sql.gz | mysql my_db --user= --password= --host=
```

```bash
USE database_name;
SOURCE path_to_sql_file;
```

Export dump

```bash
mysqldump  --skip-extended-insert my_db | gzip > DUMP_FILE.sql.gz
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

## MyTOP

Monitor the database

```bash
mytop --prompt -d database_name
```
