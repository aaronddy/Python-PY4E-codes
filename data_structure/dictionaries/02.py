# Many counters with a Dictionary
# One common use of dictionaries is counting how often we "see" something

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 2

print(ccc)



# Dictionary Tracebacks

print(ccc['csev'])
print('csev' in ccc)  # True
print('csew' in ccc)  # False


# When we see a new name
counts = dict()
names = ['joy', 'sarah', 'ann', 'Jun', 'ann', 'annie', 'joy', 'joy']
for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] += 1
print(counts)


# simplified counting with get()
for name in names:
  counts[name] = counts.get(name, 0) + 1
print(counts)