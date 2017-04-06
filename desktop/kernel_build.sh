#!/bin/bash

sudo make all
sudo make modules_install
sudo make install
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
