# Use words.txt as the file name
fname = input("Enter file name: ""C:/Users/hp/Desktop/visual studio  code assignment/romeo assignment/romeo.txt")
fh = open(fname)
for line in fh:
    linestrip=line.rstrip()
    lineup=linestrip.upper()
    print(lineup)
    
