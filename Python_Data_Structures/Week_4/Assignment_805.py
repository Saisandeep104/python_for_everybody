fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst =list()
for line in fh:
    line = line.rstrip()
    #print(line)
    if 'From ' not in line: continue
    #print(line)
    pos = line.find('From ')
    subs = line[pos:]
    #print(subs)
    val = subs.split()
    #print(len(val))
    # for email in val:
    #     if 
    #     lst.append(val[1])
    #lst.append(val[1])
    print(val[1])
    count+=1
# lst2 = list()
# for emails in lst:
#     if emails in lst2: continue
#     lst2.append(emails)

#print(len(lst))

print("There were", count, "lines in the file with From as the first word")
