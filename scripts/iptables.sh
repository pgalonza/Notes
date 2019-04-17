#! /bin/bash
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -A INPUT -s local_network -j ACCEPT
sudo iptables -A INPUT -s remote_ip -j ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -I INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP
