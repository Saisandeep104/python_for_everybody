import urllib.parse,urllib.request,urllib.error
import xml.etree.ElementTree as ET 
import re
from bs4 import BeautifulSoup

url = input("Enter url: ")
data = urllib.request.urlopen(url).read()

print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
count =0
sumCount = 0
for d in lst:
    count+=1
    sumCount += int(d.find('count').text)
print("Count:",count)
print("Sum: ",sumCount)