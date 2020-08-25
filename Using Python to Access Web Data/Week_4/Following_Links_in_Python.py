# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def newUrl(s,pos):
    html = urllib.request.urlopen(s, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    req =0
    for tag in tags:
        req+=1
        if req == int(pos):
            temp= tag.get('href', None)
    return temp



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
count = input("Enter count:")
pos = input("Enter position:")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
req = 0
s = None
name = list()
for i in range(int(count)+1):
    if s == None:
        s = url
    print(s)
    s = newUrl(s,pos)
    #name.append(re.findall('^by.+\.',s))
    #print(s)
#for w in name:
#    print(w)
            
    #for i in range(int(count)):
    
