#!/bin/bash
#find all host and update arp cache

network_id=$(ip -4 addr show eth0 | grep inet | awk -F" " {'print $2 '} | awk -F"." {'print $1 "." $2 "." $3 '})

echo -n "Starting ip: $network_id."
read startip
echo -n "Ending ip: $network_id."
read endip

echo "Scanning ip $network_id . $startip . $endip"

for((i=startip; i<=endip; i++ )); do
    ping -c 1 -w 1 "$network_id.$i"
done

clear

arp -e | grep -v incomplete > arp_cache.txt

pyt=$(python3 mac_man.py)
echo "$pyt"