import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')
lst = list()

fname = input("Enter The File name:")

for line in open(fname):
    #print(line)
    line = line.rstrip()
    if 'From: ' not in line: continue 
    #print(line)
    lst = line.split(" ")
    email = lst[1]
    org =email.split("@")
    #print(email)
    #print(len(org))
    if len(org) < 2 :continue 
    orgs = org[1]
    #print(org)
    cur.execute('''SELECT count FROM Counts WHERE org = ?''', (orgs,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org,count) VALUES ( ?,1)''',(orgs,))
    else:
        cur.execute('''UPDATE Counts SET count=count+1 WHERE org = ?''', (orgs,))
    
cur.execute('''SELECT * FROM Counts ORDER BY count''' )

sqlstr ='''SELECT * FROM Counts ORDER BY count DESC'''
cur.execute('''CREATE TABLE count_final AS SELECT * FROM Counts ORDER BY count DESC''')
sqlstr ='''SELECT * FROM count_final LIMIT 10'''
for row in cur.execute(sqlstr):
    print(row) 
conn.commit()
cur.close