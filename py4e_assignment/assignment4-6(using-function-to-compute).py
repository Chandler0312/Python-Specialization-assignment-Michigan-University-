inpH=str(input("please enter the hour:"))
inpR=str(input("please enter the rate:"))
hour=float(inpH)
rate=float(inpR)
def computepay(hour, rate):
    together=((hour-40)*1.5+40)*rate
    return together
if hour>40:
    p=computepay(hour,rate)
else:
    p=hour*rate
print("pay",p)
