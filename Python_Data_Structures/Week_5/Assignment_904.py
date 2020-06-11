name = input("Enter file:")
if len(name)< 1: name ="mbox-short.txt"
handle = open(name)
lst = list()
for lines in handle:
    lines = lines.rstrip()
    if 'From ' not in lines: continue
    val = lines.split()
    lst.append(val[1])
#print(lst)    
#print(len(lst))
large = None
count = dict()
for email in lst:
    count[email]=count.get(email,0)+1
for email in count:
    if large is None or large<count.get(email,0):
        Lemail = email
        large = count.get(email,0)

print(Lemail,large)