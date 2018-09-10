#!/bin/bash
DIR=/data/backup/`date +%Y.%m.%d`
NAME=`date +%Y.%m.%d_%H%M`

mkdir ${DIR};
tar cvpzf ${DIR}/mysql_${NAME}.tar.gz /var/lib/mysql
tar cvpzf ${DIR}/home_${NAME}.tar.gz --exclude=/home/www-data /home
mysqldump  --skip-extended-insert modx | gzip > ${DIR}/modx_${NAME}.sql.gz
echo `date +%Y.%m.%d_%H_%M` "backup - OK" >> /opt/backup/backup.log
(echo  "Subject: BACKUP"; echo `date +%Y.%m.%d` `date +%H:%M` "backup DONE";)|sendmail -f ***REMOVED*** ***REMOVED***
chown -R backup:backup /data/backup
