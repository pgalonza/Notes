# Commands

Format the flash card

```bash
mkfs -t ntfs 'Arch' -I /dev/sd*
```

Read ttyUSB0

```bash
chmod a+rw /dev/ttyUSB0
```

Encoding

```bash
iconv -f cp1251 -t utf8
file -bi
```

Search in files

```bash
find -name *.c -type f | xargs grep open

grep -R open --include="*.c".
```

Share the directory <http://$HOSTNAME:8000/>

```bash
python -m SimpleHTTPServer
```

Print shared object dependencies

```bash
ldd /path_to_object
```

Check nginx configuration

```bash
nginx -t
```

Print the locate of binary

```bash
type -a command
whereis command
which command
```

Search by commands history

```bash
Ctrl+R
```

Executing a long command

```bash
Ctrl+X,E
```

Terminal reinitialization

```bash
reset
```

Determine file type

```bash
file file_name
```

Create a new UUID value

```bash
uuidgen
```

Cd rom access

```bash
chmod u+s /usr/bin/wodim
```

Display file or file system status

```bash
stat
```

Compare files

```bash
comm
```

Merge files

```bash
paste
```

Read from standard input and write to standard output and files

```bash
tee
```

Documnentation

```bash
/usr/share/doc
```

Load one core

```bash
yes > /dev/null &
perl -e 'while(1){}'
```

Clean file

```bash
truncate -s 0 <file_name>
echo '' > <file_name>
> <file_name>
cat /dev/null > <file_name>
true | tee <file_name>
dd if=/dev/null of=<file_name>
shred <file_name>
shred -zu <file_name>
```

Translate or delete characters

```bash
tr
```

Set or retrieve a process's CPU affinity

```bash
taskset
```

## PERMISSION

```bash
usermod -u 2005 foo
groupmod -g 3000 foo

find / -group 2000 -exec chgrp -h foo {} \;
find / -user 1005 -exec chown -h foo {} \;

usermod -g <NEWGID> <LOGIN>
```

## NETSTAT

Список всех открытых портов (TCP)

```bash
netstat -at
```

Список всех открытых портов (UDP)

```bash
netstat -au
```

Список только прослушиваемых портов (TCP)

```bash
netstat -lt
```

Статистика по всем открытым портам

```bash
netstat -s
```

Подробное отображение списка с открытыми портами - добавлен PID и имя процессов

```bash
netstat -p
```

Объединим все ключи в полезную команду для просмотра открытых TCP/UDP портов с именами процессов (может понадобиться root-доступ)

```bash
netstat -ltupn
```

Список подключенных хостов

```bash
netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u
```

## TAR

Создание архива

```bash
tar cvpzf archive.tar.gz /forpack
```

Распаковка архива

```bash
tar xfvz archive.tar.gz
tar xfvj archive.tar.bz2 -C /var/www
```

Просмотр содержимого

```bash
tar -tf archive.tar
```

## DHCP

Get dhcp

```bash
dhclient -v
```

## HASH

Take sum sha1

```bash
echo -n "actual_password_here" | sha1sum | tr [:lower:] [:upper:]
```

Take sum like shadow

```bash
python3 -c "import crypt; print(crypt.crypt('actual_password_here', '\$6\$random_salt\$'))"
```

## Network

Change interface speed

```bash
ethtool -s eth0 speed 100 duplex full
```

Create a new UUID value

```bash
uuidgen eth1
```

## TREE

```bash
tree -d -L 2
```

## Open files, sockets

Show maximum of open files

```bash
cat /proc/sys/fs/file-max
```

Show allocated file descriptors, not use file descriptors, maximum of file descriptors

```bash
cat /proc/sys/fs/file-nr
```

Show the number of open files on your system

```bash
lsof | wc -l
lsof | grep 29384
lsof /home
```

Show limits of process start by user

```bash
cat /proc/PID/limits
```

Show maximum of objects inotify per user

```bash
/proc/sys/fs/inotify/max_user_instances
```

Show maximum of watch files and directories per object inotify

```bash
/proc/sys/fs/inotify/max_user_watches
```

Show maximum of events in queued

```bash
/proc/sys/fs/inotify/max_queued_events
```

Show shell process of user limits

```bash
ulimit -a
```

 Show settings

```bash
sysctl -a
```

Accept changes

```bash
sysctl -p
```

Change process limits

```bash
prlimit --pid PID --nofile=1024:1024
```

## TIME

View

```bash
timedatectl status
```

## FAIL2BAN

View

```bash
fail2ban-client status
fail2ban-client status asterisk-udp
```

Unban

```bash
fail2ban-client set asterisk-udp unbanip ip_address
```

## IPTABLES

View

```bash
iptables -n -L -v --line-numbers
```

## RAM, SWAP

Memory use

```bash
cat /proc/meminfo

ps axo rss,comm,pid \
| awk '{ proc_list[$2]++; proc_list[$2 "," 1] += $1; } \
END { for (proc in proc_list) { printf("%d\t%s\n", \
proc_list[proc "," 1],proc); }}' | sort -n | tail -n 10 | sort -rn \
| awk '{$1/=1024;printf "%.0fMB\t",$1}{print $2}'
```

## SYSTEMCTL

Systemd reload

```bash
systemctl daemon-reload
```

Restart network manager

```bash
systemctl restart NetworkManager
```

Masked/unmasked, Completely disabled service

```bash
sudo systemctl mask service_name
sudo systemctl unmask service_name
```

## Environment

```bash
export var=
export var=$var
```

## ACL

```bash
umask
```

View premissions

```bash
getfacl
```

Add default permission

```bash
setfacl -d -m u::rwx,g::r-x,o::r-x /home/test/
```

Remove default permission

```bash
setfacl -k /home/test/
```

Remove permission

```bash
setfacl -x user_name /home/test/
```

Recursive

```bash
setfacl -R
```

Remove all acl

```bash
setfacl -bn /home/test/
```

## SED

Replace in all files

```bash
sed -i 's/old_text/new_text/g' *
```

## Mount

Cifs

```bash
mount.cifs //host/share /mnt -o user=dmosk,domain=dmosk.local,vers=3.0
```

CD-rom

```bash
mount- -o loop /opt/cd.iso /opt/repo
```

Remount with rw

```bash
mount -n -o remount,rw /dev/sdXX
```

## Chromium

Proxy

```bash
chromium --proxy-server="socks://host:9050"
```

Discard

```bash
browser://discards
chrome://discards
```

Task manager

```bash
Shift + ESC
```

Chrome Flag

```bash
browser://flags/
```

GPU information

```bash
browser://gpu/
```

## Ffmpeg

Video from RTSP

```bash
ffmpeg -y -re -acodec pcm_s16le -rtsp_transport tcp -i rtsp:// -vcodec copy -af asetrate=22050 -acodec aac -b:a 96k -t 15 tmp/test.mp4
```

Screenshot from RTSP

```bash
ffmpeg -rtsp_transport tcp -i rtsp:// -f image2 -vf fps=fps=1 -t 0.001 -ss 00:00:3 tmp/image.png
```

## Youtube-dl

Best video

```bash
youtube-dl -f bestvideo+bestaudio 'url'
```

Best audio

```bash
youtube-dl -f bestaudio 'url'
```

The list of formats

```bash
youtube-dl -F 'url'
```

## Ldconfig

Create the cache

```bash
ldconfig
```

Delete the cache

```bash
rm /etc/ld.so.cache
```

View what libraries are in cache

```bash
ldconfig -p
```

## Benchmark

FIO

* Read

```bash
fio --name=randread --ioengine=libaio --iodepth=16 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

* Write

```bash
fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

* Read & Write

```bash
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=random_read_write.fio --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
```

## Grep

Print only matching parts

```bash
grep -Eo "pattern" file | sort | uniq
```

## Shutdown/Poweroff/Reboot

* Shutdown

```bash
shutdown -h hours:minutes
init 0
telinit 0
shutdown -h now
poweroff
halt --poweroff
reboot --poweroff
shytdown --poweroff
halt --no-wtmp --no-wall
```

 Cancel

```bash
shutdown -c
```

* Poweroff

```bash
halt
halt --force
reboot --halt
poweroff --halt
poweroff --force
```

* Reboot

```bash
poweroff --reboot
shutdown --reboot
reboot --force
halt --reboot
init 6
reboot
```

Problems with software

```bash
reboot -f
```

Problems with kernel, mount, libc

```bash
echo b>/proc/sysrq-trigger
```

Problems with kernel and hardware

```bash
ipmitool chassis power cycle
```

Problems with kernel and hardware without open console

```bash
ipmitool -H ipmi.server.local chassis power cycle
```

## SysRq

Unraw

```bash
Alt+SysRq+r
```

Terminate

```bash
Alt+SysRq+e
```

Kill

```bash
Alt+SysRq+i
```

Sync

```bash
Alt+SysRq+s
```

Unmount

```bash
Alt+SysRq+u
```

Reboot

```bash
Alt+SysRq+b
```

## Logrotate

Check the configuration file

```bash
logrotate -d /etc/logrotate.d/config_name
````

## Sox

Convert to VoIP format

```bash
sox -V vm-intro.wav -r 8000 -c 1 -t ul vm-intro.ulaw
sox -V vm-intro.wav -r 8000 -c 1 -t al vm-intro.alaw
sox -V vm-intro.wav -r 8000 -c 1 -t gsm vm-intro.gsm
```

## ESXI

### Network

Up or down

```bash
esxcli network nic up/down -n vmnicX
```

Set speed and duplex

```bash
esxcfg-nics -s 10000 -d full vmnicX
```

### Disk

Convert the Thin disk to Eager Zeroed Thick disk

```bash
vmkfstools --inflatedisk /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Convert the Thick disk to Eager Zeroed Thick disk

```bash
vmkfstools --eagerzero /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Check and repair vmdk

```bash
vmkfstools --fix check file_name.vmdk
vmkfstools -x check file_name.vmdk
vmkfstools -x repair file_name.vmdk
```

## Amavisd

Check the configuration file

```bash
amavisd -u amavis -c /etc/amavisd/amavisd.conf debug
```

## Udevadm

Show in realtime

```bash
udevadm monitor
```

Get attributes

```bash
udevadm info /dev/sdb1
```

## Chattr

Make immutable

```bash
chattr +i file_name
```

Show the file attributes

```bash
lsattr file_name
```

## Cache

### Clean

PageCache

```bash
sync; echo 1 > /proc/sys/vm/drop_caches
```

Inode and dentrie

```bash
sync; echo 2 > /proc/sys/vm/drop_caches
```

Inode, dentrie and PageCache

```bash
sync; echo 3 > /proc/sys/vm/drop_caches
```

Swap

```bash
swapoff -a && swapon -a
```

Percentage value controls the tendency of the kernel to reclaim
the memory which is used for caching of directory and inode objects

```bash
echo 1000 > /proc/sys/vm/vfs_cache_pressure
```

## GPG

Import key

```bash
gpg --keyserver keys.gnupg.net --recv-keys key
```

Generate key pair

```bash
gpg --full-gen-key
```

Show private keys

```bash
gpg --list-secret-keys --keyid-format LONG <email>
```

Export public key

```bash
gpg --armor --export <key_id>
```

## Slmgr

Install or replace the product key

```bash
slmgr /ipk product_key
```

Install kms host

```bash
slmgr /skms host_name:port
```

Activation windows

```bash
slmgr /ato
```

## Nmcli

Show devices

```bash
nmcli device show
```

## Fish shell

Make fish to default

```bash
echo /usr/local/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/local/bin/fish
```

Update man page completions

```bash
fish_update_completions
```

Fish settings

```bash
fish_config
```

## Entropy

View the size of the entropy pool

```bash
cat /proc/sys/kernel/random/poolsize
```

View status of server’s entropy

```bash
cat /proc/sys/kernel/random/entropy_avail
```

## RouterOS

Remove all

```bash
remove [find]
```

Show list

```bash
:foreach i in=[/interface vrrp find] do={ :put [/interface vrrp get $i name];
```

Instruction if

```bash
:if ([:len [/file find name=file_name]] > 0) do={:put "false"}
```

Print variable

```bash
:local variable_name [:len [/file find name=name_file]]; :put (variable_name);
```

## Cat

Show all symbols

```bash
cat -A file_name
```

## Systemd-analyze

Show load time

```bash
systemd-analyze
```

Show load time in detail

```bash
systemd-analyze blame
```

Write load information in svf file

```bash
systemd-analyze plot > graph.svf
```

## VirtualBox

Change UUID

```bash
VBoxManage internalcommands sethduuid disk_name.vdi
```

## Cp

Copy with attributes mode,ownership,timestamps

```bash
cp -rp /source /destination
```

Copy with save all parameters

```bash
cp -a /source /destination
```

## Shred

Overwrite a file and delete

```bash
shred -zvu -n 10 file_name
```

Overwrite a file

```bash
shred -zv -n 10 file_name
```

Overwrite a partition

```bash
shred -fvz /dev/sdXX
```

## Man

Description of the filesystem hierarchy

```bash
man hier
```

ASCII table

```bash
man ascii
```

## Curl

REST API get

```bash
curl --include --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id'
```

Formatting JSON answer

```bash
curl --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id' | python -m json.tool
```

Download file

```bash
curl --location --remote-name https://<url to file>
```

## Vim

Delete and paste

```bash
ddP
```

## Du

Show size of directories

```bash
du --max-depth=1 -h directory_name
```

Show of files

```bash
du -ah directory_name
```

Show directory size

```bash
du -sh directory_name
```

Show hidden directorys

```bash
du -hs .[^.]*
```

## Nohup

Run command immune to hangups

```bash
nohup command
```

Run command in background

```bash
nohup command &
```

## Sudo

Run shell as another user

```bash
sudo -iu user_name
sudo su - user_name command
sudo su user_name -s "/bin/bash"
```

Executing the previous command

```bash
sudo !!
```

Write command results to file with privileges

```bash
echo 1 | sudo tee -a privileged_file > /dev/null
```

## SU

Run shell as another user

```bash
su - user_name
su -l user_name
sudo su - user_name
```

## QEMU

LiveUSB

```bash
qemu-system-x86_64 -hda /dev/sdX
```

## Kubectl

Network utils

```bash
kubectl run -it --rm --image amouat/network-utils test bash
```

## Grub

Generate configyration file

```bash
grub-mkconfig -o /boot/grub2/grub.cfg
```

## Lsof

Show a list of processes that have opene files

```bash
lsof /home
```

Show a list of user processes

```bash
lsof -u <user_name>
```

Show open files in directory

```bash
lsof +D <path_to_directory>
```

Show open files of process

```bash
lsof -p <pid>
```

Show openfiles of command

```bash
lsof -c <command>
```

Show what process use port

```bash
lsof -i :<port_number>
```

## Journalctl

Unit logs in real time

```bash
journalctl -fu <unit_name>
```

## Certbot

Create certificate
_certbot.ini_

```bash
authenticator = standalone
noninteractive = true
agree-tos = true
rsa-key-size = 2048
```

```bash
certbot certonly --config ./certbot.ini --email <e-mail address> --work-dir </var/lib/letsencrypt> --config-dir <where save data> --domain <domain_name>
```

Renew certificate

```bash
certbot renew --work-dir </var/lib/letsencrypt> --config-dir <where save data>
```

## Scl

Activate python environment

```bash
scl enable rh-python<version_numver> bash
```
