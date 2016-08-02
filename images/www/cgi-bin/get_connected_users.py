#!/usr/bin/python

import commands
import os
import paramiko


x=commands.getstatusoutput("nmap -sP 192.168.43.0-255 -n| grep 'Nmap scan' | awk '{print $5}'")
count=0
for i in x[1].split('\n'):
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		client.connect(i,username='root',password='redhat')
		
		stdin,stdout,stderr=client.exec_command("lscpu | grep '^CPU(s):' ")
		for line in stdout:
			print line.split(":")[1].strip()

		stdin,stdout,stderr=client.exec_command("lscpu | grep '^CPU MHz:' ")
		for line in stdout:
			print line.split(":")[1].strip()

		stdin,stdout,stderr=client.exec_command("free -m | grep 'Mem:' ")
		for line in stdout:
			print line.split("     ")[4].strip()

		stdin,stdout,stderr=client.exec_command("df -m / | grep 'dev' | awk '{print $4}'")
		for line in stdout:
			print line.strip()
	except:
		print "Not valid connection"

	client.close()

