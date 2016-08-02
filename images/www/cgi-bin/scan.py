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

<style>
.myb
{
position:absolute;
left:50%;
}
</style>

<script type="text/javascript" src="http://192.168.43.101/css/jquery.js"></script>

<script type="text/javascript">

$(document).ready(
function(){
$("button").click(function()
		{

			
var table=document.getElementById("myt");
var nrow=document.getElementById("myt").getElementsByTagName('tr');
var dn="";var jt="";var nn="";var jt="";
url="http://192.168.43.101/cgi-bin/set.py?data=";
for(var i=1;i<nrow.length;i++)

{

	var row=table.rows[i];
	

			
	if(document.getElementById(row.id).getElementsByTagName("td")[5].getElementsByTagName('input')[0].checked==true)
	{nn=row.id;url+="nn:"+nn+"$";}

	if(document.getElementById(row.id).getElementsByTagName("td")[6].getElementsByTagName('input')[0].checked==true)
	{dn="dn:"+row.id+"$";url+=dn;}

	if(document.getElementById(row.id).getElementsByTagName("td")[7].getElementsByTagName('input')[0].checked==true)
	{jt=row.id;url+="jt:"+jt+"$";}

	if(document.getElementById(row.id).getElementsByTagName("td")[8].getElementsByTagName('input')[0].checked==true)
	{tt="tt:"+row.id+"$";url+=tt;}

}


	
	location.href=url;
	



			
		});
}
);

</script>




 	 
          </head>

	<div class="ui grey three item inverted menu">
  <a class="active item" href="../index.html">
    Home
  </a>
  <a class="item">
    What's BIG DATA ?
  </a>
  <a class="item" href="http://apache.hadoop.org">
    About Hadoop
  </a>
</div>

			  <div style="margin:6px">
			  <table id="myt" class="ui celled table" style="margin-right:3px;border:solid 1px;">
		  <thead>
		    <tr><th class="single line">S.No.</th>
		    <th>IP</th>
		    <th>CPU</th>
		    <th>Free HDD</th>
		    <th>Free RAM</th>
		    <th>NN</th>
		    <th>DN</th>
		    <th>JT</th>
		    <th>TT</th>
		    
		 
		  </tr></thead>

"""
count=1

for i in x[1].split('\n'): 
	
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(i,username='root',password='redhat')
		
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


		print "<tr id=",i,"><td>",count,"</td>"	
		print "<td>",i,"</td>"
		print "<td>",core,"Core(s) ",freq," MHz</td>"
		print "<td>",hdd," MB</td>"
		print "<td>",ram," MB</td>"
		print "<td><input name='nn' type='checkbox'></td>"
		print "<td><input name='dn' type='checkbox'></td>"
		print "<td><input name='jt' type='checkbox'></td>"
		print "<td><input name='tt'type='checkbox'></td></tr>"
		count=count+1
		client.close();
	except:
		print "<!a>"





print """
	</table>
<button class="myb">SUBMIT</button>

		 </div>
  
 				</body>
	

	</html>
"""
