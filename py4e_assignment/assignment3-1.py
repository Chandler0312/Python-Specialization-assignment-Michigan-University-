Hinp=input("enter hours:",) #Enter Hours
Rinp=input("enter rate:",) #Enter Rate
try:
    EnH=float(Hinp)
    EnR=float(Rinp)
    if EnH<=40:
       pay=float(EnH)*float(EnR)
    else:
     if EnH>40:
       pay=(float(EnH)-40)*1.5*float(EnR)+40*float(EnR)

       print("Pay:",pay)
except:
       print("please enter a number")