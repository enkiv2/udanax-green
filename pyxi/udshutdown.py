#!/usr/bin/python
# for unix of course

def main():
   port = 55146
   host = "localhost"
   xs = x88.tcpconnect(host,port)
   xs.quit()
   print "Content-type: text/html"
   print
   print "<TITLE> udanax shutfdown!</TITLE>"
   print "this should have shutdown  the backend!"

if (__name__ == "__main__"):
   main()

