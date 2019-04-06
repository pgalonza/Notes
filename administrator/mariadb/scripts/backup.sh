#!/bin/bash
DIR=/data/backup/`date +%Y.%m.%d`
NAME=`date +%Y.%m.%d_%H%M`
USER=
PASSWORD=

mkdir -p ${DIR}/${NAME}
#tar cvpzf ${DIR}/mysql_${NAME}.tar.gz /var/lib/mysql
#tar cvpzf ${DIR}/log_${NAME}.tar.gz /var/log/mysql
mysqldump -u${USER} -p${PASSWORD} --skip-extended-insert <database> | gzip > ${DIR}/<database>${NAME}.sql.gz
mariabackup --backup --target-dir=${DIR}/${NAME} --user=${USER} --password=${PASSWORD}
