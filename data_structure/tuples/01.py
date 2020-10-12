# 1.

x = ('Gleen', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y[0])
print(max(y))


# 2. 

x = [9, 8, 2]
x[2] = 6
print(x)  # [9,8,6]

y = 'ABC'
# y[2] = 'D'   //'str' object does not support item Assignment

z = (5, 4, 3)
# z[2] = 0    //'tuple' object does not support item Assignment

t = tuple()
dir(t)   # ['count', 'index']



# 5. 
(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 2)
print(a)


# 6. Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 5
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 5)]) 


# 7. 
(0, 1, 2) < (5, 1, 2)  
# 0이 5보다 작으므로 True, 0번째 인덱스만 비교하고 넘어감
(0, 1, 2000000) < (0, 3, 4) 
# 0번째 인덱스는 같으므로, 다음 첫번째 인덱스 비교. 3이 더 크므로 True. 두번째 인덱스 비교는 하지 않음
('Jones', 'Sally') < ('Jones', 'Sam')
# 'l'이 'm'보다 늦게 나오므로 
('Jones', 'Sally') > ('Adams', 'Sam')
# 'j', 'a' 비교
# 명확하게 답을 낼 수 있을 때까지만 비교