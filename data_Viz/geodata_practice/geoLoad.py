import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# api_key 변수 설정
api_key = False

if api_key is False :
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"                   # 몫데이터
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"    # geocoding api

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sqlite3 연결
conn = sqlite3.connect('geodata.sqlite3')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')    # Locations 테이블이 존재하지 않으면 테이블 생성


fh = open('where.data')
count = 0
for line in fh:
    
    # 카운트가 200이 넘으면 멈추고 다시 for loop 진행
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break      # for loop 종료

    print("count", count)
    address = line.strip()
    cur.execute('SELECT geodata FROM Locations WHERE address = ? ', (memoryview(address.encode()), ))
    # select문 시행으로 geodata 값을 부름 => 값이 없으면 try문에서 working 출력하고 다음으로 넘어감 / 있으면 try문 시행되면서 data에 geodata json이 들어감

    try:
        # print('working')
        data = cur.fetchone()[0]            # address가 DB에 이미 있어서 geodata까지 저장되어 있을 경우(이미 전 loop에서 데이터가 저장됐을 경우) data 는 해당 주소의 geodata(json)를 fetch.
        print('Found in database', address)
        continue                            # 다음 loop 으로 시작(중복된 값을 DB에 넣지 않기 위해)
    except:
        # print('pass')                       # 새로운 데이터는 try문에서 working만 출력하고 except문으로 넘어와 pass 출력 후 다음 코드르 pass 됨, 그래서 에러가 안 나는 것!
        pass

    # 딕셔너리에 address, key 넣고 urlencode로 인코딩 해 url 주소에 넣기
    params = dict()
    params['address'] = address
    if api_key is not False : params['key'] = api_key
    # print(params)                                            # {address: 하나의 address 값(line), key: 42 or 실제 api_key}
    url = serviceurl + urllib.parse.urlencode(params)        # url 변수 설정

    # url 요청 보내서 응답 받기
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()                                # 요청으로 받은 응답 데이터 디코딩해서 읽기(json형태)
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))       # 받은 데이터를 인덱스 20까지만 출력
    count += 1                                               # 들어온 url 데이터 카운팅

    try:                               # try 문 시행(status 코드를 파악하기 위해 json parsing 과정을 추가)
        js = json.loads(data)          # json parsing
        # print("trying", js)
    except:
        print(data)      # 유니코드가 에러를 일으켰을 시
        continue         # 다음 for loop 진행


    # js의 status code 확인하기
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :       # js에 'ststus'가 없거나 'status'가 ok가 아니고 zero_results가 아닐 경우엔 for loop 중단
        print('======== FAILURE TO RETRIEVE =========') 
        print(data)
        break 

    # 받은 데이터를 테이블에 넣기
    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()
    if count % 10 == 0:         # 카운팅 된 url 응답 데이터 개수가 10단위일 경우 10초간 멈춤
        print('pausing for a sleep...')
        time.sleep(5)

print('Run geodump.py to read the data from DB so you can visualize it on a map')    # for loop 종료하고 데이터베이스에 모든 데이터 저장
