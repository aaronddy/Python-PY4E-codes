# looping through strings

fruit = 'banana'
index = 0

# while loop
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# for loop
for letter in fruit:
    print(letter)

# 코드가 적을수록 좋은 이유는 뭘까? 실수를 할 가능성이 더 낮아지기 때문일까?

# looping and counting
word = 'concatenate'
count = 0
for letter in word:
    if letter == 't':
        count += 1
        print('on if',count)
print('out if',count)