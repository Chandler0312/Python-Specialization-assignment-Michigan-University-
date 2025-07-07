#grade system
score=inp=input("Enter Score: ")
try:
    if float(inp)>=0.0 and float(inp)<=1.0:
        score=float(inp)
        if float(score)>=0.9:
            print("A")
        elif float(score)>=0.8:
            print("B")
        elif float(score)>=0.7:
            print("C")
        elif float(score)>=0.6:
            print("D")
        elif float(score)<0.6:
            print("F")
    else:
        print("please enter a figure between 0.0 and 1.0")
except:
    print("please enter a figure between 0.0 and 1.0")
