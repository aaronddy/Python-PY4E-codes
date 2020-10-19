# Let's write a Web Browser!

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # socket 만들기
mysocket.connect(('data.pr4e.org', 80))   # tuple
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()   # 유니코드를 utf-8 형식으로 인코딩
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if(len(data) < 1):   # 들어오는 데이터가 없으면
        break            # 끝내기
    print(data.decode())   # utf-8을 내부 포맷인 유니코드로 디코딩
mysocket.close()