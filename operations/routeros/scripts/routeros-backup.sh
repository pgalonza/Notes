#!/bin/bash

set -x

LOGIN=<user name>
DATE=$(date +%Y-%m-%d_%k-%M-%S)

declare -A devices
devices[<name1>]=<ip address1>
devices[<name2>]=<ip address2>
devicesName=(<name1> <name2>)

function backup() {
  ssh $LOGIN@$1 "/system/backup/save dont-encrypt=yes name=$2-$DATE.backup"
  scp $LOGIN@$1:~/$2-$DATE.backup .
  ssh $LOGIN@$1 "/file remove $2-$DATE.backup"
  ssh $LOGIN@$1 "export terse verbose file=$2-$DATE"
  scp $LOGIN@$1:~/$2-$DATE.rsc .
  ssh $LOGIN@$1 "/file remove $2-$DATE.rsc"
}

for name in ${devicesName[@]}; do
        backup ${devices[$name]} $name
done
