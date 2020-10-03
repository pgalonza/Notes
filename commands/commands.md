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

Execute the command in another directory and return
```
(cd /tmp && ls)
```

Run the command at the specified time
```
echo "ls -l" | at midnight
```

Executing the previous command
```
sudo !!
```

Сommand replay
```
while true
do
command
done;
```

Automatic answer
```
yes/no | command
```

Share the directory http://$HOSTNAME:8000/
```
python -m SimpleHTTPServer
```

Execute the command without history.
```
space command
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

Write command results to file with privileges
```
echo 1 | sudo tee -a privileged_file > /dev/null
```

Executing command for each row
```
cat file_name.txt | while read in; do command_line "$in"; done
```

Sequential execution of commands
```
command_1; command_2; command_3
```

Parallel execution of commands
```
(command_1 &); (command_2 &)
```

Output one command as an argument to another
```
command_1 $(command_2)
```

Search by commands history
```
Ctrl+R
```

Usеing the argument of the last command
```
!$
````

Executing a long command
```
Ctrl+X,E
```

Terminal reinitialization
```
reset
```

Process tree
```
pstree
```

Determine file type
```
file file_name
```

Show last command execution result
```
echo $?
```

Clear command history
```
history -cw
rm ~/.bash_history
history -r
```

Don't save commands of the current session
```
unset HISTFILE
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

## TMUX
Запуск
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

Воспроизводить нажатия клавиш во всех открытых окнах
```
tmux set synchronize-panes on
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

## SSL/TLS
Import Centos
_/etc/pki/ca-trust/source/anchors/_
```
update-ca-trust
```

Import Ubuntu
_/usr/local/share/ca-certificates/_
```
update-ca-certificates
```

Check
```
openssl s_client -tls1_1 -starttls imap -connect host:143 -servername host_name
```

View
* Request CSR
```
openssl req -text -noout -verify -in domain.csr
```

* Public CRT
```
openssl x509 -text -noout -in domain.crt
```

* Private KEY
```
openssl rsa -check -in domain.key
```

Check the membership
```
openssl rsa -noout -modulus -in domain.key | openssl md5
openssl x509 -noout -modulus -in domain.crt | openssl md5
openssl req -noout -modulus -in domain.csr | openssl md5
```

Check CRT via CA
```
openssl verify -verbose -CAfile ca.crt domain.crt
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

## Dovecot
Quota
```
dovecot set quota
```

Reload the dovecot
```
doveadm reload
```

Show who connected
```
doveadm who -1
```

Clean the authorization cache
```
doveadm auth cache flush
```

## Mail
Mail console client
```
mutt -f
```

Send mail
```
(echo  "Subject: test1"; echo "test2";)|sendmail -f sender@domain.com recipient@domain.com
```

## PS
Sort by RAM
```
ps aux | sort -nk 4
ps aux —sort=%mem | grep -v 'root' | head -n 35
```

Sort by CPU
```
ps aux | sort -nk 3
ps aux —sort=%cpu | grep -v 'root' | head -n 35
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

## POSTFIX
Check configuration
```
postfix check
postconf
```

Queue view
```
mailq | less
postqueue -p | less
mailq | grep Request
find /var/spool/postfix/deferred -type f | wc -l
find /var/spool/postfix/active -type f | wc -l
find /var/spool/postfix/incoming -type f | wc –l
```

Queue send
```
postqueue -f
mailq -q
postsuper -r ALL
postqueue -i <ID-mail>
postsuper -r <ID-mail>
postqueue -s <domain>
```

Queue drop
```
postsuper -d ALL
postsuper -d deferred
postsuper -d <ID-mail>
```

Queue halt
```
postsuper -h <ID-mail>
postsuper -h ALL
postsuper -h deferred
```

Queue run
```
postsuper -H <ID-mail>
postsuper -H ALL
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

## Ansible
Start as another user
```
ansible-playbook -i host_name, -e 'ansible_ssh_user=user ansible_python_interpreter=/usr/bin/python3' --ask-pass -b --ask-become-pass ansible_user.yaml
```

Test inventory
```
ansible -i hosts.yaml all --list-hosts
```

Ping the hosts
```
ansible all -m ping
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

* Read Write
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

## OpenSSH
Generate RSA
```
ssh-keygen -f ~/name_key_file_rsa -t rsa -b 2048
```

Generate for paramiko
```
ssh-keygen -m pem -t rsa -C "test"
```

Show RSA host key
```
ssh-keyscan -t rsa host_address
```

Convert for FileZilla
```
puttygen keyname -o keyname.ppk
```

## SSH
Executing a command on a remote host
```
ssh user_name@remote_server "comamnd"
```

SOCKS-proxy
```
ssh -D 0.0.0.0:port_number user_name@remote_server
```

Port forwarding
```
ssh -L 0.0.0.0:port_number:127.0.0.1:port_number user_name@remote_server
```

Reverse SOCKS-proxy
```
ssh -v -R 0.0.0.0:port_number X.X.X.X user_name@remote_server
```

Reverse ssh tunnel
```
ssh -R 0.0.0.0:port_number:127.0.0.1:port_number X.X.X.X user_name@remote_server
```

Jumping through the remote hosts
```
ssh -J host1,host2,host3 user_name@remote_server
```

Dual ssh tunnel
```
ssh -L port_number:127.0.0.1:port_number user_name@remote_server
ssh -R port_number:127.0.0.1:port_number user_name@remote_server
```

Do not execute a remote command
```
ssh -N
```

Allows remote hosts to connect to local forwarded ports
```
ssh -g
```

Requests ssh to go to background just before command execution
```
ssh -f
```

Editing a file via scp
```
vim scp://user_name@remote_server //path_to_file
```

Mount local directory to remote host
```
sshfs user_name@remote_serve:/remote_directory /local_directory
```

## Priority
IO priority
```
ionice -c3 coommand
```

Process priority
```
nice -n 15 coommand
renice renice -n 15 -p pid
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

## Git
Edit _.gitconfig_
```
git config --global --edit
git config --global user.name
git config --global user.email
```

Stash the changes
```
git stash
git stash apply
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

## Dd
Cd rom access
```
chmod u+s /usr/bin/wodim
```

Burn the image
```
sudo dd oflag=direct status=progress  if=image.iso of=/dev/sd* bs=1M; sync
```

dd with status
```
pv -tpreb /dev/sdb | dd of=~/sdb.img bs=1M
```

Make emty files with size
```
dd if=/dev/zero of=output.dat  bs=24M  count=1
dd if=/dev/zero of=output.dat  bs=1M  count=24
```

Copy cd-rom
```
dd if=/dev/cdrom of=/opt/cd.iso bs=1M
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
sudo -su user_name command
```
