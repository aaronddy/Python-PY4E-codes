# ex 01

# x = 5
# while x > 0:
#     print(x)
#     x = x-1
# print('finish')
# print(x)


# ex 02

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done')



# ex 03 definite loop
# friends = ['joseph', 'hanna', 'mary']
# for friend in friends:
#     print('Happt New Year', friend)
# print('done')



# ex 04 finding the largest number

# largest_so_far = -1
# print('before', largest_so_far)
# for num in [9, 41, 0, 33, 54, 21, 90, 38]:
#     if num > largest_so_far:
#         largest_so_far = num
#     print(largest_so_far, num)
# print('after', largest_so_far)


# ex 05 counting in a loop

# count = 0
# print ('before:', count)
# for num in [9, 41, 0, 31, 84, 3, 10, 76]:
#     count += 1
#     print(count, num)
# print('after:', count)


# ex 06 summing up in a loop

# sumUp = 0
# print('before:', sumUp)
# for num in [9, 41, 0, 33, 54, 21, 90, 38]:
#     sumUp += num
#     print(sumUp, num)
# print('after:', sumUp)


# ex 07 finding the average in a loop

# count = 0
# sumUp = 0
# print('before:', count, sumUp)
# for num in [9, 41, 0, 33, 54, 21, 90, 38]:
#     count += 1
#     sumUp += num
#     print(count, sumUp, num)
# print('after:', count, sumUp, sumUp/count)


# ex 08 filtering in a loop

# print('before')
# for i in [9, 41, 0, 33, 54, 21, 90, 38]:
#     if i > 30:
#         print('a large number:', i)
# print('after')


# ex 09 search using a boolean variable
# found = False
# print('before', found)
# for i in [9, 41, 0, 33, 54, 21, 90, 38]:
#     if i == 21:
#         found = True
#         print(found, i)
#         break
#     print(found, i)
    
# print('after', found, i)


# ex 10 'is' and 'is not' operators

smallest = None
print('before', smallest)
for i in [9, 41, 33, 54, 21, 90, 38]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    print('smallest', smallest)
print('after', smallest)
