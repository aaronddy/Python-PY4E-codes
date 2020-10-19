# 2.
print(ord('H'))  # 72
print(ord('$'))  # 36
print(ord('w'))  # 119
print(ord('\n')) # 10


# Python 2.7.10 
x = '이광춘'
print(type(x))
# <type 'str'>
x = u'이광춘'
print(type(x))
# <type 'unicode'> 문자열이 byte이기 때문에 유니코드로 나타내고 싶으면 별도의 문자열 앞에 'u'라는 문자를 추가해야 했음




# Python 3.5.1
x = '이광춘'
print(type(x))
# <class 'str'>
x = u'이광춘'
print(type(x))
# <class 'str'> 문자열이 유니코드로 바뀌면서 'u'라는 문자를 추가해도 스트링으로 출력

#파이썬