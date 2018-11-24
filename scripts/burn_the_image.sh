#! /bin/bash
sudo dd oflag=direct status=progress  if=~/Загрузки/archlinux-2017.01.01-dual.iso of=/dev/sdc bs=1M; sync
