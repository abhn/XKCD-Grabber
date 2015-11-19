import urllib, urllib2
import os
import re

url = "http://xkcd.com/"
total = 1600 # update this to the latest

print "*** Sit back and relax. This might take a while ***"
os.system('mkdir xkcd')

for i in range(1, total):
    url_use = url + str(i)
    res = urllib2.urlopen(url_use)
    html = res.read()
    image = re.search("(?P<url>http://imgs.xkcd.com/comics/[^\s]+)", html).group("url")
    urllib.urlretrieve(image, 'xkcd/' + str(i) + '_' + image.split('/')[-1])
    print "XKCD #" + str(i) + " retrived successfully."

os.system('tar -czf xkcd.tar.gz xkcd')
os.system('rm -R xkcd')
print "File created: xkcd.tar.gz"


