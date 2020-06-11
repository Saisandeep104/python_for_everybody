largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print("Invalid Input")
        continue
   
    if largest is None: largest = num
    elif largest<num: largest = num

    if smallest is None: smallest=num
    elif smallest>num: smallest=num
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
