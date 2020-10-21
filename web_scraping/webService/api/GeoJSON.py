# 내가 아닌 다른 어떤 API 제공자가 존재, 그 API를 활용

import urllib.parse, urllib.request, urllib.error
import json

from dotenv import load_dotenv
import os
load_dotenv()

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

Key_API = os.getenv("Key_API")

while True:
  address = input('Enter locations: ')
  if len(address) < 1: break

  url = serviceurl + urllib.parse.urlencode({'address': address}) +'&key=' + Key_API   # 입력값 address 암호화해서 url에 대입

  print('Retrieving', url)
  uh = urllib.request.urlopen(url)      # url울 읽고 해독
  data = uh.read().decode()             # read()는 바이트, decode()는 문자열로 디코딩
  print('Retrieved', len(data), 'characters')

  # JSON 포맷 데이터를 json.load()를 사용하여 Python 객체로 읽어옴

  try:
      js = json.loads(data)
    
  except:
      js = None

  if not js or 'status' not in js or js['status'] != 'OK':
    print('=========== Failure to Retrieve ============')
    print(data)
    continue

  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  print('lat:', lat, 'lng:', lng)
  location = js["results"][0]["formatted_address"]
  print(location)


