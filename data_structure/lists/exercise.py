# debugging

han = open('mbox-short.txt')


for line in han:
    line = line.rstrip()
    # print("Line: ",line)
    # if line == '':
    #     print("Skip blank line")
    #     continue
    wds = line.split()
    # print("Words: ", wds)

    # Guardian Pattern a big stronger, to prevent error to happen
    # if len(wds) < 3 :   # at least 3 words
    #     continue
    # if wds[0] != 'From':
    #     # print('Ignore')
    #     continue

    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])