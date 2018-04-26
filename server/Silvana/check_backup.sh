#! /bin/bash

DIR=/data/backup/`date +%Y.%m.%d`;
NAME=`date +%Y.%m.%d_*:*`;

ETC=${DIR}/etc_${NAME}.tar.gz;
MYSQL=${DIR}/mysql_${NAME}.tar.gz;
WD=${DIR}/www-data_${NAME}.tar.gz;
OPT=${DIR}/opt_${NAME}.tar.gz;
HOME=${DIR}/home_${NAME}.tar.gz;
MODX=${DIR}/modx_${NAME}.sql.gz;
ZABBIX=${DIR}/zabbix_${NAME}.sql.gz;
LOG=${DIR}/log_${NAME}.tar.gz

if [ -e $ETC ] && [ -e $MYSQL ] && [ -e $WD ] && [ -e $OPT ] && [ -e $HOME ] && [ -e $MODX ] && [ -e $ZABBIX ] \
	&& [ -e $LOG ]; then 
	echo "1"
else
	echo "0"
fi
