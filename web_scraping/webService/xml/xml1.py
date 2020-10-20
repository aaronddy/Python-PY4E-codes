import xml.etree.ElementTree as ET

data = '''
<person>                  
  <name>Daye</name>
  <phone type='intl'>
    +10 6595 5105         
  </phone>
  <email hide='yes'/>      
</person>              
'''
# 하나의 문자열로 data 변수 생성

tree = ET.fromstring(data)   # data 스트링을 tree라는 객체에 대입
print('Name:', tree.find('name').text)      # 'name' 태그를 찾아라. 그 태그의 텍스트를 가져와라
print('Email:', tree.find('email').get('hide'))      # 'email' 태그를 찾아라. 'hide' 속성을 읽어와라