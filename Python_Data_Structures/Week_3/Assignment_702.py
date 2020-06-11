# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
val = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    count +=1
    pos = line.find(":")
    num = float(line[pos+1:])
    val +=num
print("Average spam confidence:",val/count)

#print("Done")