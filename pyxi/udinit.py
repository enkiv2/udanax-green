#!/usr/bin/python
# for unix of course
# Copyright 2005 by Roger Gregory 
# portions Copyright 1999 by Ka-Ping Yee
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions: 
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software. 
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL Ka-Ping Yee OR Udanax.com BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
# THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
# 
# Except as contained in this notice, "Udanax", "Udanax.com", and the
# transcluded-U logo shall not be used in advertising or otherwise to
# promote the sale, use or other dealings in this Software without
# prior written authorization from Udanax.com.
 
import sys, os, string, socket, x88

def main():

#   port = 55146
#   host = "localhost"
#   xs = x88.tcpconnect(host,port)
   status =	os.sytem("/usr/udanax/green/be_source/backend")
   print "Content-type: text/html"
   print
   print "<TITLE> udanax initc!</TITLE>"
   print "this should have inited the backend! status = %s" % status
 
if (__name__ == "__main__"):
   main()
 

