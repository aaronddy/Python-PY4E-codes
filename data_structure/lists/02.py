# concatenating lists using +

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a+b)  # it works
# d = a - b  ==>  TypeError
# print(d)
print(a)


# lists can be sliced using :

t = [90, 3, 25, 66, 59, 31, 4, 22]
t[1:3]  # [3, 25, 66]
t[:3]   # [90, 3, 25]
t[3:]   # [66, 59, 31, 4, 22]
t[:]    # [90, 3, 25, 66, 59, 31, 4, 22]


# list methods
x = list()
type(x)
print(dir(x))


# building a list from scratch
stuff = list()
stuff.append('book')
stuff.append('title')
print(stuff)
stuff.append('cookie')
print(stuff)


# Is somthing in a list?
some = [1, 21, 9, 30, 5]
print(9 in some)
print(33 in some)
print(20 not in some)


b = list()
while True:
    inf = input('Enter number: ')
    if inf == 'done': break
    value = float(inf)
    b.append(value)

average = sum(b) / len(b)
print('Average:', average)