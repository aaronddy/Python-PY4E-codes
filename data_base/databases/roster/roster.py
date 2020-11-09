import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Course (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id      INTEGER,
    course_id    INTEGER,
    role         INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# 조합 형태의 프라이머리 키(user_id, course_id). 한 가지의 조합만 존재 가능

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'roster_data_sample.json'

str_data = open(fname).read()
json_data = json.loads(str_data)
# print(json_data)

for item in json_data:

    name = item[0]
    title = item[1]
    role = item[2]
    
    print((name, title, role))           # 튜플로 출력

    cur.execute('''INSERT OR IGNORE INTO User (name)                    
        VALUES ( ? )''', ( name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', ( name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)                    
        VALUES ( ? )''', ( title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', ( title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES ( ?, ?, ? )''', ( user_id, course_id, role ))
    # REPLACE는 UPDATE처럼 쓰임(갱신)
    conn.commit()    # 반복문을 돌 때마다 commit을 하게 되면 비용이 덜 듦(디스크에 저장이 되기 때문)

print(len(json_data))

