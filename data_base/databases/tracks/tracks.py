import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')    # 데이터베이스에 새로운 파일 생성
cur = conn.cursor()                         # 데이터베이스와 작업하는 일종의 핸들러

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title  TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    album_id  INTEGER,
    title  TEXT UNIQUE,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text                       # found = True일 때 for loop 종료, 그 전 loop인 key가 매개변수와 동일할 때 found == True가 되면서 다음 child 태그에서 값만 갖고오고 for loop 종료
        if child.tag == 'key' and child.text == key :
            found = True
    return None


stuff = ET.parse(fname)                                    # fanme 문자열 parsing
all = stuff.findall('dict/dict/dict')                      # 원하는 모든 노드에 접근
print('Dict count: ', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None) : continue      # Track ID 가 없을 경우 다음 loop

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : continue         # name or artist or album 이 없을 경우 다음 loop

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name)                    
        VALUES ( ? )''', ( artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?', ( artist, ))
    # print("values", cur.fetchone()) ==> "values" (1,)
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', ( album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO track (title, album_id, count, rating, len)
        VALUES ( ?, ?, ?, ?, ? )''', ( name, album_id, count, rating, length ))
    # REPLACE는 UPDATE처럼 쓰임(갱신)
    conn.commit()


  
