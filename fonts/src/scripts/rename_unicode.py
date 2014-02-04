#!/usr/bin/python
# coding: UTF-8

import os
import codecs
import re
import struct

def tohex(s):
	res = ""
	for c in s:
		res += "%02X" % ord(c)
	return res

pngdir = "pngdir"
outdir = "outdir"

files = os.listdir(pngdir)

chars = list(u"あいうえお")

i = 0
for png in files:
	hex = tohex(chars[i])
	print png + " = " + chars[i] + " = uni" + hex + ".png"
	os.rename(pngdir + '/' + png, outdir + "/uni" +hex+".png")
	i = i+1
