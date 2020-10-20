import xml.etree.ElementTree as ET

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

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')   # users 태그 아래 user 태그를 가져와라
print('User count:', len(lst))   # 2

for item in lst:
    print('User Id:', item.find('id').text)
    print('User Name:', item.find('name').text)
    print('Attribute:', item.get('x'))