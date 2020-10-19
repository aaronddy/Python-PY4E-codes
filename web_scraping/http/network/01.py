# 파이썬을 이용해 네트워크 자원에 접근하는 방법을 배워보자

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )