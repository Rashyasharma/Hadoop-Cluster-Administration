#!/usr/bin/python

import commands
import cgi
import os

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


d=cgi.FormContent()
a=d['data'][0]

x=commands.getstatusoutput("hadoop fs -rm /user/apache/" + a)
 
print "<p>" + a + " Deleted Successfully</p>"




