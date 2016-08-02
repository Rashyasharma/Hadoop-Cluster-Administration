#!/usr/bin/python	

import cgi
import os
import commands
import paramiko

d=cgi.FormContent()



print "content-type:text/html\n"

a=d['data'][0].split("$")
nn=list()
dn=list()
jt=list()
tt=list()


for i in a:
	
	b=i.split(":")
	if b[0]=="nn":
		nn.append(b[1])
	if b[0]=="dn":
		dn.append(b[1])
	if b[0]=="jt":
		jt.append(b[1])
	if b[0]=="tt":
		tt.append(b[1])



file=open("myip.txt","w")

myip="[nn]\n"+nn[0]+" ansible_ssh_user=root ansible_ssh_pass=redhat\n[dn]\n"
file.write(myip)


for i in dn:
 	myip=i+" ansible_ssh_user=root ansible_ssh_pass=redhat\n"
	file.write(myip)

myip="[jt]\n"+jt[0]+" ansible_ssh_user=root ansible_ssh_pass=redhat\n[tt]\n"
file.write(myip)


for i in tt:
 	myip=i+" ansible_ssh_user=root ansible_ssh_pass=redhat\n"
	file.write(myip)

	

file.close()





hdfssitenn='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/nn</value>
</property>
<property>
<name>dfs.permissions</name>
<value>false</value>
</property>
</configuration>
'''

file=open("/var/www/cgi-bin/hdfs-site.xml","w")
file.write(hdfssitenn)
file.close

hdfssitedn='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/dn</value>
</property>
</configuration>
'''

file=open("/var/www/cgi-bin/hdfsdn/hdfs-site.xml","w")
file.write(hdfssitedn)
file.close()


coresite='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://'''+nn[0]+''':9001</value>
</property>
</configuration>
'''


file=open("/var/www/cgi-bin/core-site.xml","w")
file.write(coresite)
file.close()


mapredjt='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>'''+jt[0]+''':9002</value>
</property>
</configuration>
'''

file=open("/var/www/cgi-bin/mapredjt/mapred-site.xml","w")
file.write(mapredjt)
file.close()



mapredtt='''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>'''+jt[0]+''':9002</value>
</property>
</configuration>
'''

file=open("/var/www/cgi-bin/mapredtt/mapred-site.xml","w")
file.write(mapredtt)
file.close()

commands.getstatusoutput("ansible all -i myip.txt -a 'hadoop-daemon.sh stop namenode'")
commands.getstatusoutput("ansible all -i myip.txt -a 'hadoop-daemon.sh stop datanode'")
commands.getstatusoutput("ansible all -i myip.txt -a 'hadoop-daemon.sh stop jobtracker'")
commands.getstatusoutput("ansible all -i myip.txt -a 'hadoop-daemon.sh stop tasktracker'")
commands.getstatusoutput("ansible all -i myip.txt -a 'rm -rf /dn /nn'")

os.system("cp /var/www/cgi-bin/core-site.xml /etc/hadoop/")

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(nn[0],username='root',password='redhat')
sftp=client.open_sftp()
sftp.put('/var/www/cgi-bin/hdfs-site.xml','/etc/hadoop/hdfs-site.xml')
sftp.put('/var/www/cgi-bin/core-site.xml','/etc/hadoop/core-site.xml')
sftp.close()	
commands.getstatusoutput("ansible nn -i myip.txt -a 'hadoop namenode -format'")
commands.getstatusoutput("ansible nn -i myip.txt -a 'hadoop-daemon.sh start namenode'")
client.close()

commands.getstatusoutput("ansible all")

for i in dn:
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(i,username='root',password='redhat')
	sftp=client.open_sftp()
	sftp.put('/var/www/cgi-bin/hdfsdn/hdfs-site.xml','/etc/hadoop/hdfs-site.xml')
	sftp.put('/var/www/cgi-bin/core-site.xml','/etc/hadoop/core-site.xml')
	sftp.close()
	stdin,stdout,stderr=client.exec_command("hadoop-daemon.sh start datanode")
	client.close()

commands.getstatusoutput("ansible dn -i myip.txt -a 'hadoop-daemon.sh start datanode'")

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(jt[0],username='root',password='redhat')
sftp=client.open_sftp()
sftp.put('/var/www/cgi-bin/mapredjt/mapred-site.xml','/etc/hadoop/mapred-site.xml')
sftp.put('/var/www/cgi-bin/core-site.xml','/etc/hadoop/core-site.xml')
sftp.close()	
client.close()

commands.getstatusoutput("ansible jt -i myip.txt -a 'hadoop-daemon.sh start jobtracker'")

for i in tt:
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(i,username='root',password='redhat')
	sftp=client.open_sftp()
	sftp.put('/var/www/cgi-bin/mapredtt/mapred-site.xml','/etc/hadoop/mapred-site.xml')
	sftp.close()
	client.close()


commands.getstatusoutput("ansible tt -i myip.txt -a 'hadoop-daemon.sh start tasktracker'")

commands.getstatusoutput("hadoop fs -mkdir /user/apache/")
commands.getstatusoutput("hadoop fs -chown apache /user/apache/")
commands.getstatusoutput("hadoop fs -chmod og+rwx /user/apache/")


print '''\


 <link rel="stylesheet" href="css/semantic.css">
  <link rel="stylesheet" href="css/style.css">

<style>

.congrats

{


padding:2% 22%;


}

.congratss

{

margin:2% 39%;


}

.details
{

text-align:center;
}


</style>

<html>

 <link rel="stylesheet" href="../css/semantic.css">
  <link rel="stylesheet" href="../css/style.css">



<body>



<div class="congrats">
<img class="congratsimg" src="../images/congrats.png" >
</div>



<div class="details">

'''

print "<h2>Namenode :",nn[0],"</h2>" 
print "<h2>Jobtracker :",jt[0],"</h2>"

print "<h2>Datanodes :"

for i in dn:

	print i,"|"
print "</h2>" 

print "<h2>Tasktrackers :"

for i in tt:

	print i,"|"
print "</h2>" 
  



print '''

</div>

<div class="congratss">
<a href="http://192.168.43.101/cgi-bin/scan.py"><button class="ui blue button" >Edit My Cluster</button></a>
<a href="http://192.168.43.101/cgi-bin/dashboard.py"><button class="ui blue button">Continue.....</button></a>




</div>
</body>
</html>


'''

