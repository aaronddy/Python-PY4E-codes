# urllib를 이용해 웹 데이터 읽어오기

# Using urllib in Python
# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file.
# urllib는 연결을 만들고(socket), get 요청을 전송하고(send(cmd), 자동으로 인코딩), 새로운 줄을 보내거나 데이터를 받거나 헤더를 처리하는 등 모든 걸 다 한다.



import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())   # 모든 문자열이 bytes로 들어오면 유니코드로 디코딩

# 출력 결과에 header가 없는데 이는 .urlopen에서 이미 먹어치움.

fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand2:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)   # 문장마다 카운팅
print(counts)       # 전체 카운팅


# urllib를 이용하면 정확히 파일을 다루는 것과 동일함. 로컬에 저장된 텍스트 파일을 다루던 것처럼 네트워크를 통해 가져온 데이터를 파일화 해 불러오는 것과 같음



# Reading Web Pages(HTML)
fhand3 = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand3:
    print(line.decode().strip())
