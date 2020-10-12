# 8.
# First we sort the dictionary by the key using the items() method and sorted() function

d = {'a': 10, 'b': 1, 'c': 22}
print(d.items()) 
# >> dict_items([('a', 10), ('b', 1), ('c', 22)])  returned as a list
print(sorted(d.items()))   
# >> [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print("show", k, v)



# 9.
# we do this with a for loop that creates a list of tuples

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k,v in c.items():
    tmp.append( (v, k) )   # key, value 의 순서를 바꿔서 리스트에 append
print(tmp)   # [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)   # [(22, 'c'), (10, 'a'), (1, 'b')]  value의 순서대로 정렬 / reverse = True : 내림차순(descending)

# 이 과정을 설명하자면 c라는 딕셔너리 items()를 이용해 튜플로 바꿔 tmp 리스트에 넣어 value의 내림차순으로 정렬
 



# Even shorter version
# List Comprehension

print( sorted ( [ (v, k) for k, v in c.items() ], reverse=True ))  # value 내림차순
