#!/bin/bash
DIR=/opt/backup/`date +%Y.%m.%d`;
NAME=`date +%Y.%m.%d_%H:%M`;

mkdir ${DIR};
tar cvpzf ${DIR}/mysql_${NAME}.tar.gz /var/lib/mysql;
tar cvpzf ${DIR}/etc_${NAME}.tar.gz /etc;
tar cvpzf ${DIR}/www-data_${NAME}.tar.gz /home/www-data;
tar cvpzf ${DIR}/opt_${NAME}.tar.gz --exclude=/opt/backup /opt; 
tar cvpzf ${DIR}/home_${NAME}.tar.gz --exclude=/home/www-data /home;
mysqldump  --skip-extended-insert modx | gzip > ${DIR}/modx_${NAME}.sql.gz;
mysqldump  --skip-extended-insert zabbix | gzip > ${DIR}/zabbix_${NAME}.sql.gz;
echo `date +%Y.%m.%d_%H_%M` "backup - OK" >> /opt/backup/backup.log;
(echo  "Subject: BACKUP"; echo `date +%Y.%m.%d` `date +%H:%M` "backup DONE";)|sendmail -f ***REMOVED*** ***REMOVED***;
chown -R backup:backup /opt/backup;
