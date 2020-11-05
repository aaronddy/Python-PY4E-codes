import sqlite3

conn = sqlite3.connect('emaildb.sqlite')  # 새로운 파일 생성
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')       # 해당 파일에 Counts 테이블이 존재한다면 삭제

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')     # 이메일과 조회 수를 컬럼으로 갖는 Counts 테이블 생성

fname = input("Enter file name")
if(len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith("From: "): continue          # 'From: '으로 시작하는지 확인
    pieces = line.split()
    email = pieces[1]

    # 딕셔너리와 비슷한 작업 시작(key가 있는지 확인하고 있으면 value를 수정, 없으면 새로 생성)
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))    # <- tuple 이메일 주소가 동일한 정수형 카운트 값을 가져오기 위해 커서를 준비시키는 커맨드 / sql injecton 찾아보기
    row = cur.fetchone()    # 해당 조건을 만족하는 하나의 row를 cursor가 읽어들임
    
    if row is None:         # 테이블을 훑었는데 해당 조건에 만족하는 row가 없다면
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES (?, 1)''', (email,))            # Counts 테이블에 새로운 로우를 만드는데 이메일은 email로 조회수는 1로 넣어라
    else:
        cur.execute('UPDATE Counts SET count = count+1 WHERE email = ? ', (email,))    # 조건을 만족하는 row가 있다면 조회수를 1 높여라
    
    conn.commit()      # 메모리에 정보들을 저장하다가 모든 정보를 디스크로 옮기게 하는 커맨드


sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC'     # 실행할 커맨드

for row in cur.execute(sqlstr):
    print('Email',str(row[0]), 'Count',row[1])

cur.close()     # 커서 종료