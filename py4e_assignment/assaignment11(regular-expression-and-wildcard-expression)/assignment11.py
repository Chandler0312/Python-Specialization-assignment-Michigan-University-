#the code which extract the sum of numbers in a text using regular expression and wildcard characters
import re
digit=list()
filename=input("plz enter the file(text)name:") #filename
fil=open(filename)
for line in fil:
    line=line.rstrip()
    num=re.findall("[0-9]+",line)               #seach and print a list of strings(at least one digit number)
    if len(num)==0:                             #eliminate the empty list
        continue
    for number in num:
        digit.append(int(number))

total=sum(digit)                                #adds up all the intergers
print("sum:",total)
from bs4 import BeautifulSoup

# 测试代码
html = "<p>Hello, <b>BeautifulSoup</b>!</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())  # 输出: Hello, BeautifulSoup! 