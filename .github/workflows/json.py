#import url module
import urllib.request, urllib.parse, urllib.error
#import json module
import json
sum=0
url = http://py4e-data.dr-chuck.net/comments_42.json
print('Retrieving', url)
#uh is like a file handler holding bytes of information
uh = urllib.request.urlopen(url)
#pull out the data from file handler uh
data =  uh.read()
#total length of data is diaplayed
print('Retrieved', len(data), 'characters')
#retrieve the data using json
info = json.loads(data)
#extract list "comments"
comments=info["comments"]
print(len(comments))
for item in comments:
    sum+=item["count"]#extract count from dictionary "item" and find sum
print(sum)
