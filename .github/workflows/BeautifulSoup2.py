# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Jaise.html"
count=7
pos=18
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    position=1
    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        position+=1
        if(position==pos+1):
                url=(tag.get('href', None))
                print('Retrieving:',url)
                name=re.findall('.+_([A-za-z]+)',url)
                print(name[0])
   