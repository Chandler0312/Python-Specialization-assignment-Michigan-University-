#generate the average number in a file
name=input("please enter the file name properly:")
file=open(name)
count=0
totalfvalue=0
for line in file:
    if line.startswith("X-DSPAM-Confidence"):
        place=line.find(":")
        value=line[place+1:]
        fvalue=float(value)
        totalfvalue=totalfvalue+fvalue
    else:
        continue
    count=count+1
Asc=totalfvalue/count

print("Average spam confidence:",Asc)

