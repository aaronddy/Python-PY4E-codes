# algorithms
# a set of rules or steps used to solve a problem

# data structures
# a particular way of organizing data in a computer

# list are mutable, though strings are immutable - we can change an element of a list using the index operator

fruit = 'Banana'
#fruit[0] = 'b'  # TypeError: 'str' does not support item assignment

lotto = [2, 14, 55, 36, 96]
print(lotto)

lotto[2] = 30
print(lotto)  # [2, 14, 30, 36, 96]


# using the range function
print(range(4))   # [0, 1, 2, 3]

friends = ['Joseph', 'hanna', 'glenn']
print(len(friends))         # 3
print(range(len(friends)))  # [0, 1, 2]


