hrs = input("Enter Hours:")
#h = float(hrs)
rate = input("Enter Rates:")
#r = float(rate)
try:
    h = float(hrs)
    r =float(rate)
except:
    print("Not a number")
    quit()

if h<40:
    pay =h*r
else:
    pay =1.5*(h-40)*r+40*r
print(pay)