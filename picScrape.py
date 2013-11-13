__author__ = 'Kevin'

import praw
import urllib2
import requests
from urlparse import urlparse
import posixpath

#Parses and splits the url from submission
def get_filename_from_url(url):
    import urlparse
    url_path = urlparse.urlparse(url).path
    return url_path.split('/')[-1]

#Sets up the UserAgent and connection
user_agent = ("picScrape/1.0 by kzisme")
r = praw.Reddit(user_agent='picScrape/1.0 by kzisme')
submissions = r.get_subreddit('pics').get_hot(limit=25)
for post in submissions:
    get_filename_from_url(post.url)

#Downloading the file using urllib2
f = urllib2.urlopen(post.url)
data = f.read()
o = urlparse(post.url)
print o.path
varPath = o.path
with open(varPath, "wb")as code:
    code.write(data)



