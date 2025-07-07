#generate the largest and the smallest number in all entered numbers
thelargest=None
thesmallest=None

while True:
        num=input('please enter anumber or "done" to terminate:')
        if num =="done":
            break
        try:
            num=int(num)
            if thelargest==None or thesmallest==None:
                thelargest=num
                thesmallest=num
            elif num>thelargest:
                thelargest=num
            elif num<thesmallest:
                thesmallest=num
        except:
             print("Invalid input")
              
print('Maximum is',thelargest)
print("Minimum is",thesmallest)
