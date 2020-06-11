name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
for lines in handle:
    lines = lines.rstrip()
    if 'From ' not in lines: continue
    words = lines.split()
    #print(words)
    lst.append(words[5])
#print(lst)

hrs = list()
for time in lst:
    hour = time.split(":")
    hrs.append(hour[0])

    # hrs.append(hour[0])
#print(hrs)

dic_hour = dict()
for h in hrs:
    dic_hour[h]=dic_hour.get(h,0)+1
#print(dic_hour)
hr = dic_hour.items()
hr = sorted(hr)
for k,v in hr:
    print(k,v)
# listtt = dic_hour
# for k,v in dic_hour.items():
#     listtt.append(v,k)

# print(listtt)
