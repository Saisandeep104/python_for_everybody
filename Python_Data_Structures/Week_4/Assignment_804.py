fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    val = line.split(" ")
    for word in val:
        if word in lst: continue
        lst.append(word)   
#print(line.rstrip())
lst.sort()
print(lst)