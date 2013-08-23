#!/usr/bin/python
# Filename: httpGet.py
 
import urllib2
from bs4 import BeautifulSoup
import re
siteUrls = " "
 
url = "http://jesusjzp.github.io/"
def getContent(url):
    content = urllib2.urlopen(url).read()
    #print content
 
    soup=BeautifulSoup(content)
    global siteUrls
    siteUrls = soup.findAll('a',attrs={'class':'post'})
    #nextUrl = soup.find('div',attrs={'class':'topicListFooter'})
    #print siteUrls
    #print str(nextUrl)
    strip_tag_pat=re.compile('</?\w+[^>]*>')
 
    f = file('info.txt','w')
    for i in siteUrls:
        i0 = re.sub(strip_tag_pat,' ',str(i))
        i1 = str(i).split(' ')
        #print i1
        html = i1[2][6:-1] 
        #print html + i0
        f.write(html+i0+'\n')
    f.close()
 
 
getContent(url)
