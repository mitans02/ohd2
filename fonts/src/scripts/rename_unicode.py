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
files.sort()

# borrow from http://tagnoheya.com/charlist/charlist2.html
chars = list(u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ")

i = 0
for c in chars:
	hex = tohex(c)
	print files[i] + " = " + c + " = uni" + hex + ".png"
	os.rename(pngdir + '/' + files[i], outdir + "/uni" +hex+".png")
	i = i+1

