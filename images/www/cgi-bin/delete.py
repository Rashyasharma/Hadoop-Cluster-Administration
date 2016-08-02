#!/usr/bin/python

import commands

 
print "content-type:text/html"
print ""

print """


         <html>
	 <head>
 	 
 	 
 	 <link rel="stylesheet" href="http://192.168.43.101/css/semantic.css">

<style>
.myb
{
height:70px;
width:200px;
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
url="http://192.168.43.101/cgi-bin/deletefiles.py?data=";
for(var i=1;i<nrow.length;i++)

{

	var row=table.rows[i];
	

			
	if(document.getElementById(row.id).getElementsByTagName("td")[2].getElementsByTagName('input')[0].checked==true)
	{url+=row.id;}



}



location.href=url;
	

			
		});
}
);

</script>




 	 
          </head>

			  <div style="margin:6px">
			  <table id="myt" class="ui celled table" style="margin-right:3px;border:solid 1px;">
		  <thead>
		    <tr><th class="single line">S.No.</th>
		    <th>Name</th>
		    <th>Select</th>
		    
		 
		  </tr></thead>

"""


d=commands.getstatusoutput("hadoop fs -ls /user/apache/")

a=d[1].split("/user/apache/")
i=0
l=len(a)
count=0

while(i<l-1):
	count+=1
	i+=1
	b=a[i].split("\n")[0]
	print "<tr id=",b,"><td>",count,"</td><td>",b,"</td>"	
	print "<td><input name='rd' type='radio'/></td></tr>"		
print """
</table>


<button class="myb" style="font-size:40px;position:relative;top:40%;left:0%;">Delete</button>

</div>
</body>
</html>
"""
