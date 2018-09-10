#!/bin/bash
sudo -u nginx rm -rf /home/www-data/mysite.ru/*
sudo -u nginx cp -r * /home/www-data/mysite.ru/
