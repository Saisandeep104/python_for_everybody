import json
import urllib.request,urllib.response,urllib.parse,urllib.error


url = input("Enter Url:")
data = urllib.request.urlopen(url).read()

info = json.loads(data)
#print(info)
#print(len(info))
comments = info["comments"]
print(len(comments))
total = 0
for dataa in comments:
    total += int(dataa["count"])
print ("sum:",total)
