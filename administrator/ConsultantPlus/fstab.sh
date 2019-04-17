#!/bin/bash

firstStart=1ststart
start=ConsultantPlus
homeDir=$(pwd)

#задание параметров
echo "enter account name"
read accName
echo "set the domain"
read domain
echo "set username"
read username
echo "set password"
read -s password
echo "enter virtual disk name"
read virtDisk
echo "enter mount disk name"
read diskName

cd /home/$accName

echo "create dir /mnt/cons"
sudo mkdir /mnt/cons && sudo chmod 0777 /mnt/cons

echo "make dir and chown ok"

sudo echo "#ConsultantPlus" >> /etc/fstab
sudo echo "//host/ConsultantPlus /mnt/cons cifs _netdev,domain=$domain,username=$username,password=$password,iocharset=utf8,file_mode=0777,dir_mode=0777 0 0" >> /etc/fstab
sudo mount -a

echo "mount ok"
echo "create POL link"

touch $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo '#!/usr/bin/env playonlinux-bash' >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo '[ "$PLAYONLINUX" = "" ] && exit 0' >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo 'source "$PLAYONLINUX/lib/sources"' >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo "export WINEPREFIX=\"$homeDir/.PlayOnLinux/wineprefix/$virtDisk\"" >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo 'export WINEDEBUG="-all"' >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo "cd \"/home/name/.PlayOnLinux/wineprefix/$virtDisk/dosdevices/$diskName:\"" >> $homeDir/.PlayOnLinux/shortcuts/$firstStart
echo 'POL_Wine cons.exe /linux /group /sprocess=0 "$@"' >> $homeDir/.PlayOnLinux/shortcuts/$firstStart

touch $homeDir/.PlayOnLinux/shortcuts/$start
echo '#!/usr/bin/env playonlinux-bash' >> $homeDir/.PlayOnLinux/shortcuts/$start
echo '[ "$PLAYONLINUX" = "" ] && exit 0' >> $homeDir/.PlayOnLinux/shortcuts/$start
echo 'source "$PLAYONLINUX/lib/sources"' >> $homeDir/.PlayOnLinux/shortcuts/$start
echo "export WINEPREFIX=\"$homeDir/.PlayOnLinux/wineprefix/$virtDisk\"" >> $homeDir/.PlayOnLinux/shortcuts/$start
echo 'export WINEDEBUG="-all"' >> $homeDir/.PlayOnLinux/shortcuts/$start
echo "cd \"/home/name/.PlayOnLinux/wineprefix/$virtDisk/dosdevices/$diskName:\""  >> $homeDir/.PlayOnLinux/shortcuts/$start
echo 'POL_Wine cons.exe /linux "$@"' >> $homeDir/.PlayOnLinux/shortcuts/$start

sudo chmod -R 755 $homeDir/.PlayOnLinux/shortcuts/
sudo chown -R $accName:$accName $homeDir/.PlayOnLinux/shortcuts/

echo "<<!!DONE!!>>"
