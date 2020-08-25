import json
import sqlite3


database = sqlite3.connect("roster.sqlite")
cur = database.cursor()



cur.executescript(''' 
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

cur.executescript('''
CREATE TABLE User( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT UNIQE );
CREATE TABLE Course(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member(id INTEGER NOT NULl PRIMARY KEY AUTOINCREMENT, role INTEGER, user_id INTEGER, course_id INTEGER);
''')
#important note this 
str_data = open("roster_data.json").read()
data = json.loads(str_data)
for d in  data:
    if len(d) < 3: continue
    cur.execute(''' INSERT OR IGNORE INTO User(name) VALUES (?)''',(d[0],))
    cur.execute(''' SELECT id FROM User WHERE name = ?''',(d[0],))
    User_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Course(title) VALUES (?)''',(d[1],))
    cur.execute(''' SELECT id FROM Course WHERE title = ?''',(d[1],))
    Course_id = cur.fetchone()[0]
    cur.execute(''' INSERT OR IGNORE INTO Member(role,user_id,course_id) VALUES (?,?,?)''',(d[2],User_id,Course_id))

strs = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X'''



cur.close
database.commit()