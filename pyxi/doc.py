#!/usr/bin/python
# for unix of course

#just example stuff

import sys, os, string, socket, x88

def main():
   port = 55146
   host = "localhost"
   xs = x88.tcpconnect(host,port)
#   xs.quit()

   docid = "1.0.1.0.1" 
# def opendoc(self, docid, editable=0):
   #     """Open a document, optionally for editing."""
   mode = editable and x88.READ_WRITE or x88.READ_ONLY # zzz this is wrong
   docid = self.xs.open_document(docid, mode, x88.CONFLICT_COPY)

   self.textvspan = self.linkvspan = None
   for vspan in self.xs.retrieve_vspanset(docid):
            span = vspan.span
            if vspan.span.start[0] == 1:
                # This will break if the back-end returns more than one span.
                self.textvspan = vspan.span
            elif vspan.span.start[0] == 2:
                self.linkvspan = vspan.span
            else:
                warn("ignoring vspan %s" % vspan)

   if self.textvspan is not None:
            textvspec = x88.VSpec(docid, [self.textvspan])
            self.textspec = x88.SpecSet(textvspec)
   else:
            warn("document contains no data")

#        self.updatefwdback()
 #       self.send("opendoc")
 

#def showdoc(self):
   #     """Display the contents of a document in the text area."""
   if self.textvspan is not None:
      text = self.xs.retrieve_contents(self.textspec)[0]

   print "Content-type: text/html"
   print
   print "<TITLE> udanax doc!</TITLE>"
   print "this should be a udanax doc!"
   print text

 
 
if (__name__ == "__main__"):
   main()

