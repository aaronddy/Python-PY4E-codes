# 8.
# First we sort the dictionary by the key using the items() method and sorted() function

d = {'a': 10, 'b': 1, 'c': 22}
print(d.items()) 
# >> dict_items([('a', 10), ('b', 1), ('c', 22)])  returned as a list
print(sorted(d.items()))   
# >> [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)



# 9.
# we do this with a for loop that creates a list of tuples

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for v, k in c.items():
    tmp.append( (v, k) )
print(tmp)

