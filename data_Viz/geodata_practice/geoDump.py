import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')                    # Locations 테이블에 있는 모든 row를 select

fhand = codecs.open('where.js', 'w', 'utf-8')
fhand.write('data_locations = [\n')                       # where.js에 괄호안의 내용을 적고
count = 0

for row in cur :

    print(type(row[1]))             # bytes    
    data = str(row[1].decode())     # sql에서 들어온 bytes를 디코딩해서 string 타입으로 변경, json 형태
    print(type(row[1].decode()))    # string
    try: 
        result = json.loads(data)   # deserialization, json 문자열을 파이썬 타입(dict, list)으로 디코딩 
        # type(result)  --> dict
    except: continue

    if not('status' in result and result['status'] == 'OK'): continue

    lat = result["results"][0]["geometry"]["location"]["lat"]
    lng = result["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue

    where = result["results"][0]["formatted_address"]
    where = where.replace("'","")
    
    try:
        print(where, lat, lng)
        
        count += 1
        if count > 1 : fhand.write(',\n')
        output =  "["+str(lng)+ ","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write('\n];\n')
cur.close()
fhand.close()
print(count, 'are recoded in where.js')
print("Open where.html to see visualization on map")

