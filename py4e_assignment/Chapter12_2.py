from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

lst=list()
# Retrieve all of the span tags
tags = soup('span')           # =soup.find_all('span') 
for tag in tags:
    lst.append(tag.contents[0])

sumlst=list()
count=0
for numbers in lst:
    sumlst.append(int(numbers))
    count=count+1

print("count",count)
print("sum",sum(sumlst))