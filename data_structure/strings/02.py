# slicing strings

s = 'Monty Python'
print(s[:2])  # Mo
print(s[8:])
print(s[:])   # Monty Python
print(s[:-2]) # Monty Pyth

# using in as a logical operator

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit

if 'a' in fruit:
    print('found it')


# string library
# Python has a number of string functions which are in the string library.
# These functions do not modify the original string, instead they  return a new string that has invoked.

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi there.'.lower())

print(type(greet))
# print(dir(greet))

# stripping whitespaces
greeting = '    Hello Bob     '
greeting.lstrip()  # 'Hello Bob     '
greeting.rstrip()  # '      Hello Bob'
greeting.strip()   # 'Hello Bob'


# parsing and extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
find = data.find('@')
print(find)
take = data.find(' ', find)
print(take)
host = data[find+1 : take]
print(host)