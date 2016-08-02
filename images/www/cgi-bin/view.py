#!/usr/bin/python

import commands

 
print "content-type:text/html"
print ""

print """


         <html>
	 <head>
 	 
 	 
 	 <link rel="stylesheet" href="http://192.168.43.101/css/semantic.css">

          </head>

			  <div style="margin:6px">
			  <table id="myt" class="ui celled table" style="margin-right:3px;border:solid 1px;">
		  <thead>
		    <tr><th class="single line">S.No.</th>
		    <th>Name</th>
		    <th>Size</th>
		<th>Created</th>
		    
		 
		  </tr></thead>

"""


d=commands.getstatusoutput("hadoop fs -ls /user/apache/")
info=d[1].split()
a=d[1].split("/user/apache/")
i=0
l=len(a)
count=0
size=7
date=8
time=9

while(i<l-1):
	count+=1
	i+=1
	b=a[i].split("\n")[0]
	fsize=float(info[size])/1024/1024
	print "<tr id=",b,"><td>",count,"</td><td>",b,"</td>"	
	print "<td>",fsize," MB</td><td>",info[date]," @ ",info[time],"</td></tr>"
	size+=8
	date+=8
	time+=8	
	
print """
</table>

</div>
</body>
</html>
"""
