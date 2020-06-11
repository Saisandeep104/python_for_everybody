def computepay(h,r):
    if h>40:
        p = 1.5*(h-40)*r+40*r
    else: p = r*h
    return p

hrs = input("Enter Hours:")
rate = input("Enter the Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)