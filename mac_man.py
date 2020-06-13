try:
    from mac_vendor_lookup import MacLookup    #for mac address lookup
except ImportError as e:
    print("install mac_vendor_lookup module")

try:
    from tabulate import tabulate               #to display in a table format
except ImportError as e:
    print("install tabulate module")

import sys
import os
import subprocess

#geting mac address from the arp table
proc = subprocess.Popen(["arp -e | grep -v incomplete | awk -F \" \" {'print $3'} | grep -v HWaddress |awk -F \":\" {'print $1\":\"$2\":\"$3\":\"$4\":\"$5'}"], stdout=subprocess.PIPE, shell=True)
(mac, err) = proc.communicate()
#geting ip address from arp table 
proc = subprocess.Popen(["arp -e | grep -v incomplete | awk -F \" \" {'print $1'} | grep -v Address "], stdout=subprocess.PIPE, shell=True)
(ip, err) = proc.communicate()
#converting into a list
mac=mac.decode().split("\n")
ip=ip.decode().split("\n")

lis=list()
te=list()

for i in range(len(mac)):
    if mac[i]=="":
        continue
    te=[ip[i],mac[i],MacLookup().lookup(mac[i])]
    lis.append(te)

print(tabulate( lis,tablefmt='orgtbl',headers=['IP', 'MAC',"Ventor"]))