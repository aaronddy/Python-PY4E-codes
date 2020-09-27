# the Newline Character

stuff = 'Hello\nWorld'
stuff
print(stuff)
print(len(stuff))

stuff1 = 'X\nY'
print(stuff1)
print(len(stuff1))


# prompt for file name

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)