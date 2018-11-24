#!/bin/bash
sudo mkdir ~/Documents/scripts/`date +%Y.%m.%d`
sudo tar cvpzf ~/Documents/scripts/`date +%Y.%m.%d`/mysql_`date +%Y.%m.%d_%H_%M`.tar.gz /var/lib/mysql
sudo tar cvpzf ~/Documents/scripts/`date +%Y.%m.%d`/etc_`date +%Y.%m.%d_%H_%M`.tar.gz /etc
sudo tar cvpzf ~/Documents/scripts/`date +%Y.%m.%d`/www_`date +%Y.%m.%d_%H_%M`.tar.gz /home/www-data
#sudo tar cvpzf ~/Документы/scripts/backup/opt_`date +%Y.%m.%d_%H_%M`.tar.gz /opt
#sudo tar cvpzf ~/Документы/scripts/backup/home_`date +%Y.%m.%d_%H_%M`.tar.gz /home
sudo tar cvpzf ~/Documents/scripts/`date +%Y.%m.%d`/home__`date +%Y.%m.%d_%H_%M`.tar.gz --exclude=/home/nyanta/VirtualBox\ VMs --exclude=/home/nyanta/UnrealEngine --exclude=/home/nyanta/rpmbuild --exclude=/home/nyanta/Documents/scripts/`date +%Y.%m.%d` --exclude=/home/nyanta/.local/share/Trash --exclude=/home/nyanta/Downloads /home/nyanta
