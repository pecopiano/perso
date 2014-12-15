import urllib2
from bs4 import BeautifulSoup
import re

# Fetch the page indexing the top voted Youtube links on reddit
url = 'http://www.reddit.com/domain/youtube.com/top/?sort=top&t=all'

url_read = urllib2.urlopen(url)
content = url_read.read()

# Make it pretty.
# For some reason the subsequent regex script didn't catch the Youtube urls on the raw HTML source
soup = BeautifulSoup(content)

soup_pretty = soup.prettify()

# Encode in utf. Again, the script failed otherwise.
soup_utf = soup_pretty.encode('utf-8')

# Regex to find the video id's
youtube_id = re.findall('v=(.{11}).*', soup_utf)

# Remove duplicates
clean = [p for p in set(youtube_id)]

url = []

# Append id's to regular Youtube urls
for p in clean:
    url.append("https://www.youtube.com/watch?v=%s" %p)

# Write the resulting urls to a .txt file
write_url = "\n".join(url)

filename = open("reddit-youtube-links.txt", 'w')
filename.write(write_url)
filename.close()
