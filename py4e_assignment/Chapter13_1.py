import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2194543.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts=list()
lst = tree.findall('comments/comment')
for item in lst:
    counts.append(item.find("count").text)

nums = list()
for result in counts:
    nums.append(int(result))

print('Count:', len(nums))
print('Sum:', sum(nums))