

fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    print(lx.rstrip().upper())   # delete newline, \n