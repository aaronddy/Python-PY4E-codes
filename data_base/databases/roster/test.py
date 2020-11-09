import json

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'roster_data_sample.json'

str_data = open(fname).read()           # fname을 열어서 읽기
json_data = json.loads(str_data)        # json 파일을 읽어들인 뒤 파싱

print(json_data)

for item in json_data:                  # item 은 하나의 row

    user = item[0]
    course = item[1]
    role = item[2]
    
    print(user, course, role)


