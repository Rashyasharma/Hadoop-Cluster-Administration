#!/usr/bin/python

import os
import commands
import ansible



d=commands.getstatusoutput('ansible all -i myip.txt -a "lscpu" ')

print "content-type:text/html\n"

print "<p>",d,"</p>"
