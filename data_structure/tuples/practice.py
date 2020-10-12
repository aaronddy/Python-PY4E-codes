# The top 10 most common words

fhand = open('concept.txt', "r", encoding='utf-8')

counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  
# print(counts)

lst = list()
for k, v in counts.items():
  newtup = (v, k)
  lst.append(newtup)
print(lst)   # tuple을 list에 append

lst = sorted(lst, reverse=True)   # value 를 기준으로 내림차순

for v,k in lst[:10]:   # 상위 10번째까지 
  print(v, k)