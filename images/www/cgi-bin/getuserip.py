#!/usr/bin/python
import os

print "content-type:text/html"
print ""

cip = os.environ['REMOTE_ADDR']

print "Your Ip is :" + cip


