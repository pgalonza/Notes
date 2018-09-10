#! /bin/bash

DIR=/opt/backup

find ${DIR} -type d -mtime +21 -exec rm -rf {} \;
