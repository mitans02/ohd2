#!/usr/bin/python
# coding: UTF-8
import httplib
import re
import pprint

# borrow from http://tagnoheya.com/charlist/charlist2.html
chars = list(u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ")

def fetch(file, url):
	c = httplib.HTTPConnection("www.fileformat.info")
	c.request("GET", url)

	data = c.getresponse().read()

	outfile = open(file, 'wb')
	outfile.write(data)
	outfile.close()

def tohex(s):
	res = ""
	for c in s:
		res += "%02X" % ord(c)
	return res

def find_char_num(hexc):
	i = 0
	for c in chars:
		if tohex(c).lower() == hexc:
			return i
		i = i + 1

def crawl_char_image(host, path):
	extracted = {}
	conn = httplib.HTTPConnection(host)
	conn.request("GET", path)

	res = conn.getresponse()
	html = res.read().decode("UTF-8")
	conn.close()

	r = re.compile(r"src=\"(.+/char\/(.+)\/.+?\.png)")

	for mat in r.finditer(html):
		uhex = mat.group(2).rstrip().lower()

		extracted[uhex] = mat.group(1)

	return extracted


hexchars = {};
for c in chars:
	hexchars[tohex(c).lower()] = 0

hiraganas = crawl_char_image("www.fileformat.info", "/info/unicode/block/hiragana/images.htm")
katakanas = crawl_char_image("www.fileformat.info", "/info/unicode/block/katakana/images.htm")

allchars = dict(hiraganas, **katakanas)

pprint.pprint(allchars)

for uhex in allchars.keys():
	if hexchars.has_key(uhex) == False :
		print uhex + " is ignored"
		continue

	num = str(find_char_num(uhex))

	print 'save/' + num + '.png'
	fetch('save/' + num + '.png', allchars[uhex])
	hexchars[uhex] = 1


for k in hexchars.keys():
	if hexchars[k] == 0:
		print "ERROR: "+k+" is not downloaded"
