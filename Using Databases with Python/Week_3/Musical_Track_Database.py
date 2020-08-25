import sqlite3
import xml.etree.ElementTree as ET 

dataBase = sqlite3.connect('MusicLibraryDB.sqlite')
cur = dataBase.cursor()


cur.executescript('''
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Album(id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,artist_id   INTEGER, title TEXT UNIQUE);
CREATE TABLE Genre(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Artist(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Track(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE,album_id   INTEGER,genre_id   INTEGER, len INTEGER, rating INTEGER, count INTEGER);

''')

def datas(d,attri):
    present = False
    for child in d:
        if present: return child.text
        if child.tag == "key" and child.text == attri:
            present = True
    return None



fhandle = open("tracks/Library.xml")
tree =ET.parse(fhandle)
data = tree.findall("dict/dict/dict")    
#print(len(data))
for dicts in data:
    #print("Hello world")
    #print("There are totlal this ? many child tags are here",len(dicts))
    Track_Title = datas(dicts,"Name")
    Artist_Name = datas(dicts,"Artist")
    Genre_Type = datas(dicts,"Genre")
    Album_Title = datas(dicts,"Album")
    lenn = datas(dicts,"Total Time")
    count = datas(dicts, 'Play Count')
    rating = datas(dicts, 'Rating')
    if Artist_Name == None or Album_Title == None or Genre_Type== None or Track_Title == None or lenn == None or count == None or rating == None: continue
    #print(Track_Title,Album_Title,Artist_Name,Genre_Type)
    cur.execute('''INSERT OR IGNORE INTO Genre(name) VALUES(?)''',(Genre_Type,))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''',(Genre_Type,))
    Genre_Id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Artist(name) VALUES(?)''',(Artist_Name,))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''',(Artist_Name,))
    Artist_Id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id  ) VALUES(?,?)''',(Album_Title,Artist_Id))
    cur.execute('''SELECT id FROM Album WHERE title = ?''',(Album_Title,))
    Album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Track(title,album_id  ,genre_id  ,len,count,rating) VALUES(?,?,?,?,?,?)''',(Track_Title,Album_id,Genre_Id,lenn,count,rating))

    
    # for child in dicts:
    #     if(child.tag != "key"): continue
    #     print(child.text)
    # for child in dicts:
    #     print()

s = '''SELECT Track.title,Artist.name,Album.title,Genre.name FROM Track JOIN Artist JOIN Album JOIN Genre ON Track.genre_id   = Genre.id AND Track.album_id  =Album.id AND Album.artist_id  =Artist.id ORDER BY Artist.name LIMIT 3'''

for row in cur.execute(s):
    print(row)
cur.close()
dataBase.commit()