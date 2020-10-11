# 1. Counting pattern

counts = dict()

print('Enter a line of text')
line = input('')

words = line.split()
print("Words", words)

for word in words:
  counts[word] = counts.get(word, 0) + 1
print(counts)



# 2. Definite loops and dictionaries

counts = {'chuck': 1, 'fred': 44, 'jane':101}
for k in counts:
  print(k, counts[k])

print(list(counts))   # ['chuck', 'fred', 'jane']
print(counts.keys())  # dict_keys(['chuck', 'fred', 'jane'])
print(counts.values())  # dict_values([1, 44, 101])
print(counts.items())   # dict_items([('chuck', 1), ('fred', 44), ('jane', 101)])  tuple..?



# Bonus: Two Iteraion variables

jjj = {'hana': 100, 'daye': 92.3, 'dohee': 1}
for aaa, bbb in jjj.items():
  print(aaa, bbb)

# hana 100
# daye 92.3
# dohee 1



name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1


bigCount = None
bitWord = None

for word, count in counts.items():
  if bigCount is None or count > bigCount:
    bigWord = word
    bigCount = count

print(bigWord, bigCount)
