import re
num =0
count =0
doc = open("regex_sum_585262.txt")
lst = list()
for line in doc:
    line = line.rstrip()
    lst = re.findall('[0-9]+',line)
    if len(lst) == 0: continue
    #print(lst)
    for w in lst:
        count+=1
        num += int(w)
    #print(count)
print(num)
#Shortest way
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )