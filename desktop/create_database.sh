#!/bin/bash
echo "CREATE DATABASE `my_db` CHARACTER SET utf8 ***REMOVED***LLATE utf8_general_ci;" | mysql
echo "CREATE USER 'name'@'localhost' IDENTIFIED BY 'password';" | mysql
echo "GRANT ALL PRIVILEGES ON `db`.* TO 'name'@'localhost';" | mysql
echo "mysql FLUSH PRIVILEGES;" | mysql
echo "RENAME USER 'modx'@'localhost' TO 'modx'@'%';" | mysql
