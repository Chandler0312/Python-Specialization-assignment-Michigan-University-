import urllib.request
import json

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

nums=[]
info = json.loads(data)
for item in info['comments']:
    nums.append(int(item['count']))

print(f"Count:{len(nums)}")    
print(f"Sum:{sum(nums)}")