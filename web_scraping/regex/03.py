# 1. Extracting a host name - using 'find' and string slicing

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16  2008'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

# 2. the Double Split Pattern
# : sometimes we split a line one way, and then grap one of the pieces of the line and split that piece again

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16  2008'

words = line.split()
print(words)  # ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

email = words[1]  # 'stephen.marquard@uct.ac.za'

pieces = email.split('@')
print(pieces)   # ['stephen.marquard', 'uct.ac.za']

host = pieces[1]
print(host)  # uct.ac.za


# 3. the Regex Expression

import re

lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16  2008'
y = re.findall('@([^ ]*)', lin)   # [^ ] ==> 공백이 아닌 문자열(공백빼고 다 가능), * ==> 그것들의 연장(0번 이상)
print(y)


# 3-1. Even cooler version

z = re.findall('^From .*@([^ ]*)', lin)
print(z) 



# 4. Escape Character, 특수문자를 문자 자체로 쓰고 싶을 때
# If you want a special regular expression character to just behave noamally(most of the time), you prefix it with '\'
# 특수문자를 문자 자체로 쓰고 싶을 때는 '\'를 접두사로 쓰면 그냥 문자로 접근할 수 있다

x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+?', x)  # non-greedy matching
z = re.findall('\$[0-9.]+', x)   # greedy matching
print(y)  # ['$1']   
print(z)  # ['$10.00']