import re
hand = open('mbox-short.txt')
numlist = list()

for line in hand:
  line = line.rstrip()
  stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
  # print(stuff)
  if len(stuff) != 1: continue
  # print(stuff)  # 값이 있는 리스트들만 추출
  num = float(stuff[0])   # 리스트에 있는 스트링에서 숫자로 전환
  # print(num)
  numlist.append(num)
# print(numlist)
print("Maximum: ", max(numlist))   # 0.9907