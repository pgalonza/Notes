#!/bin/sh

while read number; do

cat <<EOF  >  /var/spool/asterisk/$number

Channel: Local/$number
Callerid: $number
MaxRetries: 1
RetryTime: 20
WaitTime: 30
Context: conference
Extension: s
Priority: 1
Archive: yes
Set: CDR(userfield)=${REASON}
Account: confrence_1
EOF

    chown asterisk:asterisk /var/spool/asterisk/$number
    mv /var/spool/asterisk/$number  /var/spool/asterisk/outgoing

    echo "$number"

    number=`expr $number + 1`

    while [ "$?" -eq "0" ]

    do
count_files ()

{

    count_f=`ls /var/spool/asterisk/outgoing | wc -l`

        if [ "$count_f" -eq "15" ]; then

            sleep 10

            return 0

        else

            return 1

        fi

}


    count_files

    done


done < /var/spool/asterisk/list.txt

exit 0 
