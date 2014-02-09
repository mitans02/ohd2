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

for img in files:
	matches = re.search(r"uni(\w+).png", img)
	char = unichr(int(matches.group(1), 16)).encode('utf-8')
	print "<tr><td>%s</td><td><img src='%s/%s' width='50px'></td></tr>" % (char, outdir, img)

print "</table></body></html>"
