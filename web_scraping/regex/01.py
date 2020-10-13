# Using re.search() like find()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find("From: ") >= 0:
        print("find", line)


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("From: ", line):
        print("re.search", line)



# Using re.search() like startswith()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith("From: "):
        print("startswith", line)


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("^From: ", line):   # 정규식 사용
        print("^", line)