#! /bin/bash
echo "install"

wget -q "http://deb.playonlinux.com/public.gpg" -O - | sudo apt-key add -

sudo wget http://deb.playonlinux.com/playonlinux_precise.list -O /etc/apt/sources.list.d/playonlinux.list

sudo apt-get update
sudo apt-get install -y \
wine \
winbind \
winetricks \
playonlinux \
xterm

echo "<<!!DONE!!>>"
