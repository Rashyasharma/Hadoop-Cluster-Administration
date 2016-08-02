#!/usr/bin/python	

import cgi
import os
import commands
import paramiko

d=cgi.FormContent()



print "content-type:text/html\n"
print """
<head>
<script type="text/javascript" src="http://192.168.43.101/css/jquery.js"></script>

<script type="text/javascript">

$(document).ready(
function(){
location.href="http://192.168.43.101/cgi-bin/view.py";
		
}
);

</script>
 </head>
"""

cmd="hadoop fs -put /files/"+d['data'][0]+" /user/apache/"
commands.getstatusoutput(cmd)
print "<p style='position:absolute;top:50%;left:50%;'>Refreshing ...</p>"



