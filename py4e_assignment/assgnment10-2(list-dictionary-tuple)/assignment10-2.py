#more complex application of list dictionary and tuple
time=list()  #chop the right time strings
hour=list()  #chop the hour digit out
pairhour=dict()  #create a dictionary contians the hour as key and the frequency as value
l=list()
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
mbox = open(name)
for line in mbox:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    time.append(words[5])

for twodigits in time:
    hour.append(twodigits[:2])   #extract the hour digit

for eachhour in hour:
    pairhour[eachhour]=pairhour.get(eachhour,0)+1  #contruct the hour-frequency pair as dictionary

tuppairhour=list(pairhour.items())
outcome=sorted(tuppairhour)

for key,value in outcome:
    print(f"{int(key):02d}",value)




