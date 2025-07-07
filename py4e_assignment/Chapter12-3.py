from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL:")                    # original URL
position = input("Enter position:") 
count = input("Enter count:")                # looping times
for tag in range(int(count)):
    html = urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[int(position)-1].get("href",None)    # new URL after looping and extraction

print("Retrieving:",url)

   

    

