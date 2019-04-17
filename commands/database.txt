###### Create database
```
echo "CREATE DATABASE `my_db` CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql
```

###### Create user
```
echo "CREATE USER 'name'@'localhost' IDENTIFIED BY 'password';" | mysql
```

###### Give privileges for user
```
echo "GRANT ALL PRIVILEGES ON `db`.* TO 'name'@'localhost';" | mysql
```

###### Reloads the privileges
```
echo "FLUSH PRIVILEGES;" | mysql
```

###### Edit user account
```
echo "RENAME USER 'name'@'localhost' TO 'name'@'%';" | mysql
```

###### Last entry
```
SELECT MAX(`my_table`) FROM my_db;
```

###### Set password for user
```
echo "ALTER USER 'name'@'localhost' IDENTIFIED BY 'MyNewPass';" | mysql
```

###### Delete user
```
echo "DROP USER 'name'@'localhost';" | mysql
```

###### User as root privileges
```
echo "GRANT ALL PRIVILEGES ON *.* TO 'name'@'%' with GRANT OPTION;" | mysql
```

###### Give backup privileges for user
```
echo "GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'name'@'localhost'" | mysql
```

###### Import dump
```
gunzip < DUMP_FILE.sql.gz | mysql my_db --user= --password= --host=
```

###### Export dump
```
mysqldump  --skip-extended-insert my_db | gzip > ${DIR}/zabbix_${NAME}.sql.gz
```
