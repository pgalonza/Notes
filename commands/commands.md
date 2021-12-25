# Commands

Format the flash card
```
mkfs -t ntfs 'Arch' -I /dev/sd*
```

Read ttyUSB0
```
chmod a+rw /dev/ttyUSB0
```

Encoding
```
iconv -f cp1251 -t utf8
file -bi
```

Search in files
```
find -name *.c -type f | xargs grep open

grep -R open --include="*.c".
```

Share the directory http://$HOSTNAME:8000/
```
python -m SimpleHTTPServer
```

Print shared object dependencies
```
ldd /path_to_object
```

Check nginx configuration
```
nginx -t
```

Print the locate of binary
```
type -a command
whereis command
which command
```

Search by commands history
```
Ctrl+R
```

Executing a long command
```
Ctrl+X,E
```

Terminal reinitialization
```
reset
```

Determine file type
```
file file_name
```

Create a new UUID value
```
uuidgen
```

Cd rom access
```
chmod u+s /usr/bin/wodim
```

Display file or file system status
```
stat
```

Compare files
```
comm
```

Merge files
```
paste
```

Read from standard input and write to standard output and files
```
tee
```

Documnentation
```
/usr/share/doc
```

Load one core
```
yes > /dev/null &
```

Clean file
```
truncate -s 0 <file_name>
echo '' > <file_name>
> <file_name>
cat /dev/null > <file_name>
true | tee <file_name>
dd if=/dev/null of=<file_name>
shred <file_name>
shred -zu <file_name>
```

## PERMISSION
```
usermod -u 2005 foo
groupmod -g 3000 foo

find / -group 2000 -exec chgrp -h foo {} \;
find / -user 1005 -exec chown -h foo {} \;

usermod -g <NEWGID> <LOGIN>
```

## NETSTAT
Список всех открытых портов (TCP)
```
netstat -at
```

Список всех открытых портов (UDP)
```
netstat -au
```

Список только прослушиваемых портов (TCP)
```
netstat -lt
```

Статистика по всем открытым портам
```
netstat -s
```

Подробное отображение списка с открытыми портами - добавлен PID и имя процессов
```
netstat -p
```
Объединим все ключи в полезную команду для просмотра открытых TCP/UDP портов с именами процессов (может понадобиться root-доступ)
```
netstat -ltupn
```

Список подключенных хостов
```
netstat -lantp | grep ESTABLISHED |awk '{print $5}' | awk -F: '{print $1}' | sort -u
```

## TAR
Создание архива
```
tar cvpzf archive.tar.gz /forpack
```

Распаковка архива
```
tar xfvz archive.tar.gz
tar xfvj archive.tar.bz2 -C /var/www
```

Просмотр содержимого
```
tar -tf archive.tar
```

## DHCP
Get dhcp
```
dhclient -v
```

## HASH
Take sum sha1
```
echo -n "actual_password_here" | sha1sum | tr [:lower:] [:upper:]
```

Take sum like shadow
```
python3 -c "import crypt; print(crypt.crypt('actual_password_here', '\$6\$random_salt\$'))"
```

## Network

Change interface speed
```
ethtool -s eth0 speed 100 duplex full
```

Create a new UUID value
```
uuidgen eth1
```

## TREE
```
tree -d -L 2
```

## Open files, sockets

Show maximum of open files
```
cat /proc/sys/fs/file-max
```

Show allocated file descriptors, not use file descriptors, maximum of file descriptors
```
cat /proc/sys/fs/file-nr
```

Show the number of open files on your system
```
lsof | wc -l
lsof | grep 29384
lsof /home
```

Show limits of process start by user
```
cat /proc/PID/limits
```

Show maximum of objects inotify per user
```
/proc/sys/fs/inotify/max_user_instances
```

Show maximum of watch files and directories per object inotify
```
/proc/sys/fs/inotify/max_user_watches
```

Show maximum of events in queued
```
/proc/sys/fs/inotify/max_queued_events
```

Show shell process of user limits
```
ulimit -a
```

 Show settings
```
sysctl -a
```

Accept changes
```
sysctl -p
```

Change process limits
```
prlimit --pid PID --nofile=1024:1024
```

## TIME
View
```
timedatectl status
```

## FAIL2BAN
View
```
fail2ban-client status
fail2ban-client status asterisk-udp
```

Unban
```
fail2ban-client set asterisk-udp unbanip ip_address
```

## IPTABLES
View
```
iptables -n -L -v --line-numbers
```

## RAM, SWAP
Memory use
```
cat /proc/meminfo

ps axo rss,comm,pid \
| awk '{ proc_list[$2]++; proc_list[$2 "," 1] += $1; } \
END { for (proc in proc_list) { printf("%d\t%s\n", \
proc_list[proc "," 1],proc); }}' | sort -n | tail -n 10 | sort -rn \
| awk '{$1/=1024;printf "%.0fMB\t",$1}{print $2}'
```

## SYSTEMCTL
Systemd reload
```
systemctl daemon-reload
```

Restart network manager
```
systemctl restart NetworkManager
```

Masked/unmasked, Completely disabled service
```
sudo systemctl mask service_name
sudo systemctl unmask service_name
```

## Environment
```
export var=
export var=$var
```

## ACL
```
umask
```

View premissions
```
getfacl
```

Add default permission
```
setfacl -d -m u::rwx,g::r-x,o::r-x /home/test/
```

Remove default permission
```
setfacl -k /home/test/
```

Remove permission
```
setfacl -x user_name /home/test/
```

Recursive
```
setfacl -R
```

Remove all acl
```
setfacl -bn /home/test/
```

## SED
Replace in all files
```
sed -i 's/old_text/new_text/g' *
```

## Mount
Cifs
```
mount.cifs //host/share /mnt -o user=dmosk,domain=dmosk.local,vers=3.0
```

CD-rom
```
mount- -o loop /opt/cd.iso /opt/repo
```

Remount with rw
```
mount -n -o remount,rw /dev/sdXX
```

## Chromium
Proxy
```
chromium --proxy-server="socks://host:9050"
```

Discard
```
browser://discards
chrome://discards
```

Task manager
```
Shift + ESC
```

Chrome Flag
```
browser://flags/
```

GPU information
```
browser://gpu/
```

## Ffmpeg
Video from RTSP
```
ffmpeg -y -re -acodec pcm_s16le -rtsp_transport tcp -i rtsp:// -vcodec copy -af asetrate=22050 -acodec aac -b:a 96k -t 15 tmp/test.mp4
```

Screenshot from RTSP
```
ffmpeg -rtsp_transport tcp -i rtsp:// -f image2 -vf fps=fps=1 -t 0.001 -ss 00:00:3 tmp/image.png
```

## Youtube-dl
Best video
```
youtube-dl -f bestvideo+bestaudio 'url'
```

Best audio
```
youtube-dl -f bestaudio 'url'
```

The list of formats
```
youtube-dl -F 'url'
```

## Ldconfig
Create the cache
```
ldconfig
```

Delete the cache
```
rm /etc/ld.so.cache
```

View what libraries are in cache
```
ldconfig -p
```

## Benchmark
FIO
* Read
```
fio --name=randread --ioengine=libaio --iodepth=16 --rw=randread --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

* Write
```
fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=4 --runtime=240 --group_reporting
```

* Read & Write
```
fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=random_read_write.fio --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75
```

## Grep
Print only matching parts
```
grep -Eo "pattern" file | sort | uniq
```

## Shutdown/Poweroff/Reboot
* Shutdown
```
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
```
shutdown -c
```

* Poweroff
```
halt
halt --force
reboot --halt
poweroff --halt
poweroff --force
```

* Reboot
```
poweroff --reboot
shutdown --reboot
reboot --force
halt --reboot
init 6
reboot
```

Problems with software
```
reboot -f
```

Problems with kernel, mount, libc
```
echo b>/proc/sysrq-trigger
```

Problems with kernel and hardware
```
ipmitool chassis power cycle
```

Problems with kernel and hardware without open console
```
ipmitool -H ipmi.server.local chassis power cycle
```

## SysRq
Unraw
```
Alt+SysRq+r
```

Terminate
```
Alt+SysRq+e
```

Kill
```
Alt+SysRq+i
```

Sync
```
Alt+SysRq+s
```

Unmount
```
Alt+SysRq+u
```

Reboot
```
Alt+SysRq+b
```

## Logrotate
Check the configuration file
```
logrotate -d /etc/logrotate.d/config_name
````

## Sox
Convert to VoIP format
```
sox -V vm-intro.wav -r 8000 -c 1 -t ul vm-intro.ulaw
sox -V vm-intro.wav -r 8000 -c 1 -t al vm-intro.alaw
sox -V vm-intro.wav -r 8000 -c 1 -t gsm vm-intro.gsm
```

## ESXI
### Network
Up or down
```
esxcli network nic up/down -n vmnicX
```

Set speed and duplex
```
esxcfg-nics -s 10000 -d full vmnicX
```

### Disk
Convert the Thin disk to Eager Zeroed Thick disk
```
vmkfstools --inflatedisk /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Convert the Thick disk to Eager Zeroed Thick disk
```
vmkfstools --eagerzero /vmfs/volumes/DatastoreName/VMName/VMName.vmdk
```

Check and repair vmdk
```
vmkfstools --fix check file_name.vmdk
vmkfstools -x check file_name.vmdk
vmkfstools -x repair file_name.vmdk
```

## Amavisd
Check the configuration file
```
amavisd -u amavis -c /etc/amavisd/amavisd.conf debug
```

## Udevadm
Show in realtime
```
udevadm monitor
```

Get attributes
```
udevadm info /dev/sdb1
```

## Chattr
Make immutable
```
chattr +i file_name
```

Show the file attributes
```
lsattr file_name
```

## Cache
### Clean
PageCache
```
sync; echo 1 > /proc/sys/vm/drop_caches
```

Inode and dentrie
```
sync; echo 2 > /proc/sys/vm/drop_caches
```

Inode, dentrie and PageCache
```
sync; echo 3 > /proc/sys/vm/drop_caches
```

Swap
```
swapoff -a && swapon -a
```

Percentage value controls the tendency of the kernel to reclaim
the memory which is used for caching of directory and inode objects
```
echo 1000 > /proc/sys/vm/vfs_cache_pressure
```

## GPG
Import key
```
gpg --keyserver keys.gnupg.net --recv-keys key
```

## Slmgr
Install or replace the product key
```
slmgr /ipk product_key
```

Install kms host
```
slmgr /skms host_name:port
```

Activation windows
```
slmgr /ato
```

## Nmcli
Show devices
```
nmcli device show
```

## Fish shell
Make fish to default
```
echo /usr/local/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/local/bin/fish
```

Update man page completions
```
fish_update_completions
```

Fish settings
```
fish_config
```

## Entropy
View the size of the entropy pool
```
cat /proc/sys/kernel/random/poolsize
```

View status of server’s entropy
```
cat /proc/sys/kernel/random/entropy_avail
```

## RouterOS
Remove all
```
remove [find]
```

Show list
```
:foreach i in=[/interface vrrp find] do={ :put [/interface vrrp get $i name];
```

Instruction if
```
:if ([:len [/file find name=file_name]] > 0) do={:put "false"}
```

Print variable
```
:local variable_name [:len [/file find name=name_file]]; :put (variable_name);
```

## Cat
Show all symbols
```
cat -A file_name
```

## Systemd-analyze
Show load time
```
systemd-analyze
```

Show load time in detail
```
systemd-analyze blame
```

Write load information in svf file
```
systemd-analyze plot > graph.svf
```

## VirtualBox
Change UUID
```
VBoxManage internalcommands sethduuid disk_name.vdi
```

## Cp
Copy with attributes mode,ownership,timestamps
```
cp -rp /source /destination
```

Copy with save all parameters
```
cp -a /source /destination
```

## Shred
Overwrite a file and delete
```
shred -zvu -n 10 file_name
```

Overwrite a file
```
shred -zv -n 10 file_name
```

Overwrite a partition
```
shred -fvz /dev/sdXX
```

## Man
Description of the filesystem hierarchy
```
man hier
```

ASCII table
```
man ascii
```

## Curl
REST API get
```
curl --include --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id'
```

Formatting JSON answer
```
curl --location --request GET 'https://site_name/?fields=parameter_name' --header 'Authorization: OAuth id' | python -m json.tool
```

## Vim
Delete and paste
```
ddP
```

## Du
Show size of directories
```
du --max-depth=1 -h directory_name
```

Show of files
```
du -ah directory_name
```

Show directory size
```
du -sh directory_name
```

Show hidden directorys
```
du -hs .[^.]*
```

## Nohup
Run command immune to hangups
```
nohup command
```

Run command in background
```
nohup command &
```

## Sudo

Run shell as another user
```
sudo -iu user_name
sudo su - user_name command
sudo su user_name -s "/bin/bash"
```

Executing the previous command
```
sudo !!
```

Write command results to file with privileges
```
echo 1 | sudo tee -a privileged_file > /dev/null
```

## SU

Run shell as another user
```
su - user_name
su -l user_name
sudo su - user_name
```

## QEMU

LiveUSB
```
qemu-system-x86_64 -hda /dev/sdX
```

## Kubectl

Network utils
```
kubectl run -it --rm --image amouat/network-utils test bash
```

## Grub

Generate configyration file
```
grub-mkconfig -o /boot/grub2/grub.cfg
```

## Lsof

Show a list of processes that have opene files
```
lsof /home
```

Show a list of user processes
```
lsof -u <user_name>
```

Show open files in directory
```
lsof +D <path_to_directory>
```

Show open files of process
```
lsof -p <pid>
```

Show openfiles of command
```
lsof -c <command>
```

Show what process use port
```
lsof -i :<port_number>
```

## Journalctl

Unit logs in real time
```
journalctl -fu <unit_name>
```

## Certbot

Create certificate
_certbot.ini_
```
authenticator = standalone
noninteractive = true
agree-tos = true
rsa-key-size = 2048
```

```
certbot certonly --config ./certbot.ini --email <e-mail address> --work-dir </var/lib/letsencrypt> --config-dir <where save data> --domain <domain_name>
```

Renew certificate
```
certbot renew --work-dir </var/lib/letsencrypt> --config-dir <where save data>
```

## Chage

Show password expiration date
```

chage -l <user_name>
```

## Scl

Activate python environment
```
scl enable rh-python<version_numver> bash
```
