import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('track.sqlite')
cur = conn.cursor()

##创建新table
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT UNIQUE
);
CREATE TABLE Genre(
  id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name TEXT UNIQUE
);
CREATE TABLE Album(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  artist_id INTEGER,
  title TEXT UNIQUE
);
CREATE TABLE Track(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  album_id INTEGER,
  genre_id INTEGER,
  title TEXT UNIQUE,
  len INTEGER,
  rating INTEGER,
  count INTEGER 
);
''')

def sear(d,key):
    test = False
    a=0
    for i in d:
        if test:
            return i.text
        if i.tag == 'key' and i.text == key:
            test = True
    return None

fname = input('pleasse in put a filename----->')
if len(fname)<=0 :
    fname = 'Library.xml'
fdata = ET.parse(fname)
stuff = fdata.findall('dict/dict/dict')
print('Dict count:', len(stuff))
for entry in stuff:
    if (sear(entry,'Track ID') is None):continue
    name = sear(entry, 'Name')
    album = sear(entry, 'Album')
    artist = sear(entry,'Artist')
    genre = sear(entry,'Genre')
    len = sear(entry,'Total Time')
    rating = sear(entry,'Rating')
    count = sear(entry,'Play Count')
    if name is None or artist is None or genre is None or album is None  :

        continue

    print(name,'-' ,artist,'-', album,'-', count,'-', rating,'-', genre,'-',len)
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album(title,artist_id) VALUES (?,?)''', (album, artist_id,))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre(name) VALUES ( ? )''',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track(album_id,genre_id,title,len,rating,count)
                  VALUES (?,?,?,?,?,?)''',(album_id,genre_id,name,len,rating,count,))
    cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.id and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
    conn.commit()
