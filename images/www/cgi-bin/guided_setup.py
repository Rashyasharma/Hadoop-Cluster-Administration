#!/usr/bin/python

import commands
import paramiko
import os
x=commands.getstatusoutput("nmap -sP 192.168.43.0-255 -n| grep 'Nmap scan' | awk '{print $5}'")
  

print "content-type:text/html"
print ""

print """


         <html>
	 <head>
 	 
 	 
 	 <link rel="stylesheet" href="http://192.168.43.101/css/semantic.css">
 	 
          </div>

			  <div style="margin:6px">
			  <table class="ui celled table" style="margin-right:3px;border:solid 1px;">
		  <thead>
		    <tr><th class="single line">S.No.</th>
		    <th>IP</th>
		    <th>CPU</th>
		    <th>Free HDD</th>
		    <th>Free RAM</th>
		    <th>NN</th>
		    <th>DN</th>
		    
		 
		  </tr></thead>

"""
count=1
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.43.130',username='root',password='redhat')
		
stdin,stdout,stderr=client.exec_command("lscpu | grep '^CPU(s):' ")
for line in stdout:
	core=line.split(":")[1].strip()
stdin,stdout,stderr=client.exec_command("lscpu | grep '^CPU MHz:' ")
for line in stdout:
	freq=line.split(":")[1].strip()
stdin,stdout,stderr=client.exec_command("free -m | grep 'Mem:' ")
for line in stdout:
	ram=line.split("     ")[4].strip()
stdin,stdout,stderr=client.exec_command("df -m / | grep 'dev' | awk '{print $4}'")
for line in stdout:
	hdd=line.strip()


print "<tr><td>",count,"</td>"	
print "<td>","192.168.43.103","</td>"
print "<td>",core,"Core(s) ",freq," MHz</td>"
print "<td>",hdd," MB</td>"
print "<td>",ram," MB</td>"
print "<td><input type='radio'></td>"
print "<td><input type='radio'></td></tr>"
count=count+1





print """
	</table>

		 </div>
  
 				</body>
	

	</html>
"""
