# General
###### Кодировка
```
iconv -f cp1251 -t utf8

file -bi
```

###### Поиск по файлам
```
find -name *.c -type f | xargs grep open

grep -R open --include="*.c".
```
###### dd c отображением статуса
```
pv -tpreb /dev/sdb | dd of=~/sdb.img bs=1M
```

###### Выполнение команды в другой директории и возврат
```
(cd /tmp && ls)
```

###### Команда в указанное время
```
echo "ls -l" | at midnight
```

###### Выполнение предыдущей команды
```
sudo !!
```

###### IO priority
```
ionice -c3
```

###### Сommand replay
```
while true
do
command
done;
```

###### Automatic answer
```
yes/no | command
```

###### Share directory http://$HOSTNAME:8000/
```
python -m SimpleHTTPServer
```

###### Execute the command, without history.
```
space command
```

###### Print shared object dependencies
```
ldd /path_to_object
```
###### Check nginx configuration
```
nginx -t
```

# PERMISSION
```
usermod -u 2005 foo
groupmod -g 3000 foo

find / -group 2000 -exec chgrp -h foo {} \;
find / -user 1005 -exec chown -h foo {} \;

usermod -g <NEWGID> <LOGIN>
```

# NETSTAT

###### Список всех открытых портов (TCP)
```
netstat -at
```

###### Список всех открытых портов (UDP)
```
netstat -au
```

###### Список только прослушиваемых портов (TCP)
```
netstat -lt
```

###### Статистика по всем открытым портам
```
netstat -s
```

###### Подробное отображение списка с открытыми портами - добавлен PID и имя процессов
```
netstat -p
```
###### Объединим все ключи в полезную команду для просмотра открытых TCP/UDP портов с именами процессов (может понадобиться root-доступ)
```
netstat -ltupn
```

###### Список подключенных хостов
```
netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u
```

# TAR

###### Создание архива
```
tar cvpzf archive.tar.gz /forpack
```

###### Распаковка архива
```
tar xfvz archive.tar.gz
tar xfvj archive.tar.bz2 -C /var/www
```

###### Просмотр содержимого
```
tar -tf archive.tar
```

# TMUX

###### Запуск
```
tmux attach || tmux new -s session1
```
```
Ctrl+b c — создать окошко;
Ctrl+b 0...9 — перейти в такое-то окошко;
Ctrl+b p — перейти в предыдущее окошко;
Ctrl+b n — перейти в следующее окошко;
Ctrl+b l — перейти в предыдущее активное окошко (из которого вы переключились в текущее);
Ctrl+b & — закрыть окошко (а можно просто набрать exit в терминале).

Ctrl+b % — разделить текущую панель на две, по вертикали;
Ctrl+b " — разделить текущую панель на две, по горизонтали (это кавычка, которая около Enter, а не Shift+2);
Ctrl+b →←↑↓ — переходить между панелями;
Ctrl+b x — закрыть панель (а можно просто набрать exit в терминале).
```

###### Воспроизводить нажатия клавиш во всех открытых окнах
```
tmux set synchronize-panes on
```

# DHCP

###### Get dhcp
```
dhclient -v
```

# HASH

###### Take sum sha1
```
echo -n "actual_password_here" | sha1sum | tr [:lower:] [:upper:]
```
###### Take sum like shadow
```
python -c 'import crypt; print crypt.crypt("actual_password_here", "$6$random_salt$")'
```

# SSL/TLS

###### Import
/etc/pki/ca-trust/source/anchors/
```
update-ca-trust
```

###### Check
```
openssl s_client -tls1_1 -starttls imap -connect host:143 -servername host_name
```

###### View
Request CSR
```
openssl req -text -noout -verify -in domain.csr
```

Public CRT
```
openssl x509 -text -noout -in domain.crt
```

Private KEY
```
openssl rsa -check -in domain.key
```

###### Check the membership
```
openssl rsa -noout -modulus -in domain.key | openssl md5
openssl x509 -noout -modulus -in domain.crt | openssl md5
openssl req -noout -modulus -in domain.csr | openssl md5
```

###### Check CRT via CA
```
openssl verify -verbose -CAfile ca.crt domain.crt
```

# Network

###### Change interface speed
```
ethtool -s eth0 speed 100 duplex full
```

###### Create a new UUID value
```
uuidgen eth1
```

# TREE
```
tree -d -L 2
```

# Open files, sockets

###### Show maximum of open files
```
cat /proc/sys/fs/file-max
```

###### Show allocated file descriptors, not use file descriptors, maximum of file descriptors
```
cat /proc/sys/fs/file-nr
```

###### Show the number of open files on your system
```
lsof | wc -l
lsof | grep 29384
```

###### Show limits of process start by user
```
cat /proc/PID/limits
```

###### Show maximum of objects inotify per user
```
/proc/sys/fs/inotify/max_user_instances
```

###### Show maximum of watch files and directories per object inotify
```
/proc/sys/fs/inotify/max_user_watches
```

###### Show maximum of events in queued
```
/proc/sys/fs/inotify/max_queued_events
```

###### Show shell process of user limits
```
ulimit -a
```

###### Show settings
```
sysctl -a
```

###### Accept changes
```
sysctl -p
```

###### Change process limits
```
prlimit --pid PID --nofile=1024:1024
```

# TIME

###### View
```
timedatectl status
```

# FAIL2BAN

###### View
```
fail2ban-client status
fail2ban-client status asterisk-udp
```

###### Unban
```
fail2ban-client set asterisk-udp unbanip ip_address
```

# IPTABLES

###### View
```
iptables -n -L -v --line-numbers
```

# Dovecot
###### Quota
```
dovecot set quota
```
###### Reload the dovecot
```
doveadm reload
```

###### Show who connected
```
doveadm who -1
```

# Authorization cache
```
doveadm auth cache
```

# Make files

###### Make emty files with size
```
dd if=/dev/zero of=output.dat  bs=24M  count=1
dd if=/dev/zero of=output.dat  bs=1M  count=24
```

# Mail

###### Mail console client
```
mutt -f
```

# Reboot

###### Problems with software
```
reboot -f
```

###### Problems with kernel, mount, libc
```
echo b>/proc/sysrq-trigger
```

###### Problems with kernel and hardware
```
ipmitool chassis power cycle
```

###### Problems with kernel and hardware without open console
```
ipmitool -H ipmi.server.local chassis power cycle
```

# PS

###### Sort by RAM
```
ps aux | sort -nk 4
```

###### Sort by CPU
```
ps aux | sort -nk 3
```

# RAM, SWAP

###### Memory use
```
cat /proc/meminfo

ps axo rss,comm,pid \
| awk '{ proc_list[$2]++; proc_list[$2 "," 1] += $1; } \
END { for (proc in proc_list) { printf("%d\t%s\n", \
proc_list[proc "," 1],proc); }}' | sort -n | tail -n 10 | sort -rn \
| awk '{$1/=1024;printf "%.0fMB\t",$1}{print $2}'
```

# SYSTEMCTL

###### Systemd reload
```
systemctl daemon-reload
```

# Environment
```
export var=
export var=$var
```

# POSTFIX
```
postfix check
postconf
```

###### Queue view
```
mailq | less
postqueue -p | less
mailq | grep Request
find /var/spool/postfix/deferred -type f | wc -l
find /var/spool/postfix/active -type f | wc -l
find /var/spool/postfix/incoming -type f | wc –l
```

###### Queue send
```
postqueue -f
mailq -q
postsuper -r ALL
postqueue -i <ID-mail>
postsuper -r <ID-mail>
postqueue -s <domain>
```

###### Queue drop
```
postsuper -d ALL
postsuper -d deferred
postsuper -d <ID-mail>
```

###### Queue halt
```
postsuper -h <ID-mail>
postsuper -h ALL
postsuper -h deferred
```

###### Queue run
```
postsuper -H <ID-mail>
postsuper -H ALL
```

# ACL
```
umask
```

###### View premissions
```
getfacl
```

###### Add default permission
```
setfacl -d -m u::rwx,g::r-x,o::r-x /home/test/
```

###### Remove default permission
```
setfacl -k /home/test/
setfacl -R -k /home/test/
```

###### Remove permission
```
setfacl -x user_name /home/test/
```

# SED

###### Replace in all files
```
sed 's/old_text/new_text/g' *
```

# Mount

###### Cifs
```
mount.cifs //host/share /mnt -o user=dmosk,domain=dmosk.local,vers=3.0
```

# Chromium

###### Proxy
```
chromium --proxy-server="socks://host:9050"
```

# Ansible

###### Start as another user
```
ansible-playbook -i host_name, -e 'ansible_ssh_user=user' --ask-pass -b --ask-become-pass ansible_user.yaml
```

# Disks and partitions

###### View
```
fdisk -l
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT
lsblk -f
```

###### Tell the Linux kernel about the presence and numbering of on-disk partitions, update the specified partitions
```
partx -u /dev/sda
```

###### Inform the OS of partition table changes
```
partprobe
```

###### Re-scan disk
```
find /sys -iname 'scan'
echo 1>/sys/class/block/sda/device/rescan
```

SCSI
```
echo "- - -" > /sys/class/scsi_host/hostX/scan
```

###### Copy partition
```
dd if=/dev/sda of=/dev/sdb
```

###### Copy partition table
MBR
```
sfdisk -d /dev/sda | sfdisk /dev/sdb
```

GPT sda to sdb
```
sgdisk -R=/dev/sdb /dev/sda
```

###### Formatting
```
mkfs.ext4 /dev/sda
```

###### Partition synchronization
```
rsync -avzr /var/log/ /mnt/
```

###### What kind of process working with partition
```
lsof | grep '/var/log'
```

# S.M.A.R.T

###### View
```
smartctl -a /dev/sda
```

###### File system resize
```
resize2fs /dev/sda
```

# Raid

###### Information
```
cat /proc/mdstat
```

###### Add disk
```
mdadm --manage /dev/md_number --add /dev/sda
```

###### Create the raid with one disk
```
mdadm --create --verbose /dev/md_number --level=1 --raid-devices=1 /dev/sda
```

###### Change number of disks
```
mdadm --grow /dev/m_number --raid-devices=2
```

# Ffmpeg

###### Video from RTSP
```
ffmpeg -y -re -acodec pcm_s16le -rtsp_transport tcp -i rtsp:// -vcodec copy -af asetrate=22050 -acodec aac -b:a 96k -t 15 tmp/test.mp4
```

###### Screenshot from RTSP
```
ffmpeg -rtsp_transport tcp -i rtsp:// -f image2 -vf fps=fps=1 -t 0.001 -ss 00:00:3 tmp/image.png
```

# Youtube-dl

###### Best video
```
youtube-dl -f bestvideo+bestaudio 'url'
```

###### Best audio
```
youtube-dl -f bestaudio 'url'
```

###### The list of formats
```
youtube-dl -F 'url'
```

# Ldconfig
###### Create the cache
```
ldconfig
```

###### Delete the cache
```
rm /etc/ld.so.cache
```

###### View what libraries are in cache
```
ldconfig -p
```

# Benchmark
##### Disk

###### FIO
Read
```
fio --name=randread --ioengine=libaio --iodepth=16 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

Write
```
fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

Read Write
```
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=random_read_write.fio --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75

# Grep
###### Print only matching parts
```
grep -Eo "pattern" file | sort | uniq
```

# e2fsprogs
##### The defragmentation check ext4 partition
```
e4defrag -c /dev/sda
```
##### Defragmentation ext4 partition
```
e4defrag /dev/sda
```

##### Check the result ⩽0.3% non-contiguous
```
fsck -n /dev/sda
```
