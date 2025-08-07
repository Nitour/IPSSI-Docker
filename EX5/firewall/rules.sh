#!/bin/sh

# Flush rules
iptables -F
iptables -X

# Default deny
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback
iptables -A INPUT -i lo -j ACCEPT

# Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP (Flask via nginx)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

iptables -A INPUT -p tcp --dport 5000 -j ACCEPT

# Allow Mongo Express via nginx
iptables -A INPUT -p tcp --dport 8081 -j ACCEPT

# Block external access to MongoDB (27017)
iptables -A INPUT -p tcp --dport 27017 -j DROP

# Allow internal Docker network
iptables -A INPUT -s 172.0.0.0/8 -j ACCEPT

# Log dropped packets
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: " --log-level 4

exec "$@"
