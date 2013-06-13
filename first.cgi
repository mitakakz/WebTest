#!/usr/bin/python

print "Content-Type: text/html"     # HTML is following
print "\n\n"                              # blank line, end of headers

import cgi
import cgitb
cgitb.enable()

print "<HTML>"
print "<HEAD>"

print "<TITLE>CGI script output</TITLE>"
print "</HEAD>"

print "<BODY>"
print "<H1>This is my first CGI script</H1>"

form = cgi.FieldStorage()



print "Hello, " , form["name"].value
print "</BODY>"
print "</HTML>"