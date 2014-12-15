import urllib2
from bs4 import BeautifulSoup
import re
import csv

url = 'http://www.reddit.com/domain/youtube.com/top/?sort=top&t=all'

url_read = urllib2.urlopen(url)
content = url_read.read()

soup = BeautifulSoup(content)

soup_pretty = soup.prettify()

soup_utf = soup_pretty.encode('utf-8')

match = re.findall('v=(.{11}).*', soup_utf)

clean = [p for p in set(match)]

url = []

for p in clean:
    url.append("https://www.youtube.com/watch?v=%s" %p)

for p in url:
	print p

urlss = "\n".join(url)

filename = open("reddit.txt", 'w')
filename.write(urlss)
filename.close()

# with open('eggs.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(urlss)
# 
