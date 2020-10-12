fname = input('Enter file: ')
if len(fname) < 1 : fname = 'word.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:

        # idiom: retrieve/ create/ update counter
        di[w] = di.get(w, 0) + 1

# print(di)

tmp = list()
for k, v in di.items():
    newtup = (v,k)   # create new tuple
    tmp.append(newtup)
# print(tmp)

tmp = sorted(tmp, reverse=True)
# print("Descending", tmp[:5])

for v, k in tmp[:5]:
    print(k, v)


# 굳이 튜플로 변경해서 sorting 하는 이유 ==> 리스트보다 튜플을 이용하는 게 훨씬 효율적이기 때문
