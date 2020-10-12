fname = input('Enter file: ')
if len(fname) < 1 : fname = 'word.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)

    # for w in wds:
    #     print(w)
    #     if w in di:
    #         di[w] = di[w] + 1
    #         print('**Existing**')
    #     else:
    #         di[w] = 1
    #         print('**NEW**')
    #     print(di[w])
    # print(di)

    for w in wds:

        # if the key is not there, the count is zero
        # oldCount = di.get(w, 0)
        # print(w, 'old', oldCount)
        # newCount = oldCount + 1
        # di[w] = newCount

        # idiom: retrieve/ create/ update counter
        di[w] = di.get(w, 0) + 1
        # print(w, 'count', di[w])

print(di)



# now we want to find the most common word
largest = -1
theWord = None
for k, v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        theWord = k    # capture, remember the key that was the largest
        
print(theWord, largest)
