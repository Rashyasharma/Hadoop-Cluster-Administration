#!/usr/bin/python
import commands

x=commands.getstatusoutput("nmap -sP 192.168.43.0-255 -n|grep 'Nmap scan'|awk '{print $5}' ")
print x
