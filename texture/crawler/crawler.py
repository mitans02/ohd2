import httplib
import re

def fetch(file, url):
	c = httplib.HTTPConnection("www.fileformat.info")
	c.request("GET", url)

	data = c.getresponse().read()

	outfile = open(file, 'wb')
	outfile.write(data)
	outfile.close()


conn = httplib.HTTPConnection("www.fileformat.info")
conn.request("GET", "/info/unicode/block/hiragana/images.htm")

res = conn.getresponse()
html = res.read().decode("UTF-8")

r = re.compile(r"src=\"(.+/char\/(.+)\/.+?\.png)")

conn.close()

for mat in r.finditer(html):
	print 'save/' + mat.group(2).rstrip() + '.png'
	fetch('save/' + mat.group(2).rstrip() + '.png', mat.group(1))

