#find all different word in a file then put them in a list
allwords=list()
lst=list()
filename=input("plz enter the file name:")
romeotext=open(filename)
for line in romeotext:
    line=line.rstrip()
    words=line.split()
    for word in words:
        allwords.append(word)
for word in allwords:
    if word in lst:
        continue
    else:
        lst.append(word)
lst.sort()
print(lst)

    