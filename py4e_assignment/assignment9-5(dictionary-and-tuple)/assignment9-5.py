#generate the frequency of a name emerged the store the frequecy and name in a dictionary as key-value pair
frequency=dict()
name=list()
handle = open("mbox-short.txt")
for line in handle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    name.append(words[1])       #extend() will split strings into letters, while append() insert the whole string
for human in name:              # you mistaked on indented again you idiot!!!!!!!!!
    frequency[human]=frequency.get(human,0)+1

#generate the most frequent name using tuple
maxperson=None
max=0
for person,value in frequency.items():
    if value>=max or max==0:
        max=value
        maxperson=person

print(maxperson,max)


 

    