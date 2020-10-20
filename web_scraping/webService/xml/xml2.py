import xml.etree.ElementTree as ET   # xml 모듈

input = '''
<stuff>                  
  <users>
    <user x='2'>
      <id>001</id>
      <name>Daye</name>
    </user>
    <user x='7'>
      <id>009</id>
      <name>Aaron</name>
    </user>
  </users>     
</stuff>              
'''

stuff = ET.fromstring(input)      # input 스트링을 parsing해서 stuff 객체로 대입
lst = stuff.findall('users/user')   # users 태그 아래 user 태그를 가져와라/ 리스트의 형태로 두개의 user 태그가 들어감
print('User count:', len(lst))   # 2

for item in lst:
    print('User Id:', item.find('id').text)
    print('User Name:', item.find('name').text)
    print('Attribute:', item.get('x'))