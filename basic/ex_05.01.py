count = 0
sumUp = 0


while True:
    value = input('Enter a number: ')
    
    if value == 'done':
        break
    
    try:
        trans = float(value)
    except:
        print('Invalid type')
        continue
        # count -= 1
        # sumUp -= trans
        # continue로 대체하면서 다시 상단의 while loop으로 이동하므로 count, sumUp 의 값 변동이 없음

    count += 1
    sumUp += trans
    # print("Enter a number:",trans)

print('All done')
print(count, sumUp, sumUp/count)
