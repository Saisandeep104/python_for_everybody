score =input("Enter the Score:")
try:
    s = float(score)
except:
    print("Not a number")
    quit()

if(s>10):
    print("Out of range")
elif(s<0):
    print("Out of range")
elif(s>=.9): print("A")
elif(s>=.8): print("B")
elif(s>=.7): print("C")
elif(s>=.6): print("D")
elif(s<.6): print("F")
