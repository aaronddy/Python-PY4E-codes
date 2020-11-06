import xml.etree.ElementTree as ET

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'test.xml'

def lookup(d, key):
    found = False
    for child in d:
        print('before if child.text', child.text)
        if found : return child.text     # for loop에서 return을 넣으면 for문이 다 끝나지 않아도 조건이 충족되면(found = True) for loop 종료
                                         # child는 key뿐 아니라 모든 태그를 child이므로 for loop은 모든 태그에 대해 적용. 단지 원하는 key의 다음 태그 값을 가져오기 위해 True/False를 지정해 return으로 원하는 값만 추출하기 위함
        print('found = false', child.text)
        if child.tag == 'key' and child.text == key : found = True
        print('for end', child.text)    
    return None                          # found = True 인 경우가 없다면 결국 None return

stuff = ET.parse(fname)
all = stuff.findall('dict/dict')
print('Dict count: ', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None) : continue     # None 이 들어오면 다음 entry로 loop
    print('find the value!')


'''
Dict count:  3
before if child.text Track ID
found = false Track ID
for end Track ID
before if child.text 369
find the value!
before if child.text Track ID
found = false Track ID
for end Track ID
before if child.text 375
find the value!
before if child.text Track ID
found = false Track ID
for end Track ID
before if child.text 377
find the value!
'''