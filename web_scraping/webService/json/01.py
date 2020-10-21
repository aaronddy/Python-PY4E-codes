import json   # using json in python 

data = '''{
  "name": "Daye",
  "phone": {
    "type": "intl",
    "number": "+10 6595 5105"
  },
  "email": {
    "hide": "yes" 
  }
}
'''

info = json.loads(data)      # load의 's'는 스트링을 의미 / info = dictionary
print(type(info))            # dict
print('Name:', info["name"])     # Daye
print('Email:', info['email']['hide'])   # yes

# JSON represents data as nested "lists" and "dictionaries"
# 구조가 xml보다 간단
# 딕셔너리, 리스트 혹은 딕셔너리를 포함한 딕셔너리를 반환하기 때문에 xml 처럼 'get', 'find', 'findalls', 'lookup' 을 사용할 필요가 없음.


input = '''[
  {
    "id": "002",
    "x": "10",
    "name": "Daye"
  },
  {
    "id": "009",
    "x": "20",
    "name": "Aaron"
  }
]'''

info2 = json.loads(input)      # json module 이 문자열로 작성된 json 객체 리스트를 파이썬의 딕셔너리 리스트로 parsing해서 파이썬의 딕셔너리처럼 사용가능하게 함. 
print("input count:", len(info2))
print(type(info2))  # list
for item in info2:
  print('Name:', item["name"])
  print('Id:', item["id"])
  print('Attribute', item['x'])