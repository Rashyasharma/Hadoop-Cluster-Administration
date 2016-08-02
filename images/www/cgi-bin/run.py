#!/usr/bin/python	

import cgi
import os
import commands


d=cgi.FormContent()
a=d['data'][0].split("$")
fname=a[0]
mapper=a[1]
reducer=a[2]
cmd="hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -file /files/programs/"+mapper+" -mapper /files/programs/"+mapper+" -file /files/programs/"+reducer+" -reducer /files/programs/"+reducer+" -input /user/apache/"+fname+" -output /user/apache/out/"

commands.getstatusoutput("hadoop fs -rmr /user/apache/out/")
commands.getstatusoutput(cmd)
a=commands.getstatusoutput("hadoop fs -cat /user/apache/out/part-00000")

a=a[1]
a=a.replace("\n","<br/>")
a=a.replace("\t","   ")
print "content-type:text/html\n"
print "<p>",a,"</p>"
