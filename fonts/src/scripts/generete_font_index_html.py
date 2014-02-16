#!/usr/bin/python
# coding: UTF-8

import os
import codecs
import re
import struct

outdir = "outdir"

files = os.listdir(outdir)
files.sort()

print """\
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<body>
<style>
table, td, tr {
    font-size: 50px;
    border: 1px solid black;
}
</style>
<table>
"""

i = 0
for img in files:
	matches = re.search(r"uni(\w+).png", img)
	char = unichr(int(matches.group(1), 16)).encode('utf-8')
        if ( i % 10 == 0 ):
             print "<tr>"
	print "<td>%s</td><td><img src='%s/%s' width='50px'></td>\n" % (char, outdir, img)
        if ( i % 10 == 9 ):
             print "</tr>"
	i = i + 1

print "</tr></table></body></html>"
