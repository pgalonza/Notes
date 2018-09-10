#! /bin/bash

DIR=/data/backup/`date +%Y.%m.%d`
NAME=`date +%Y.%m.%d_*:*`

ETC=${DIR}/etc_${NAME}.tar.gz
MYSQL=${DIR}/mysql_${NAME}.tar.gz

if [ -e $ETC ] && [ -e $MYSQL ] \
	&& [ -e $LOG ]; then 
	echo "1"
else
	echo "0"
fi
