# 1. Matching and extracting data

# re.search() returns a True/False depending on whether the string matches the regular expression
# If we really want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2. favorite numbers are 19$ and 42'
y = re.findall('[0-9]+.', x)
print(y)    # ['2.', '19$', '42']

z = re.findall('[ae]+.', x)
print(z)


# 2. Warning: Greedy matching
# The repeat characters(* and +) push outward in both directions(greedy) to match the largest possible string

import re
a = 'From: Using the : character'
b = re.findall('^F.+:', a)
print(b) # ['From: Using the :']  why not 'From:'?   ==> 'Using the :'까지 포함해서 더 긴 문자열을 반환하는 데 이걸 탐욕적 매칭이라고 함



# 3. Non-greedy matching
# Not all regular expression repeat codes are greedy. If you add a '?' character, the (+ and *) chill out a bit...

a = 'From: Using the : character'
c = re.findall('^F.+?:', a)  # `.+?` ==> one or more characters but not greedy
print(c)  # ['From:'] not greedy, 가장 짧은 문자열을 반환

# 보통은 탐욕적인 게 기본이고 탐욕적이지 않은 게 선택 사항


# 4. Fine-tuning string expression, 더 섬세한 문자열 추출
# You can refine the match for re.findall() and separately determing which portion of the match is to be extracted by the parentheses

x = 'stephen.marquard@uct.ac.za Sat Jan  5 09:14:16  2008'
y = re.findall('\S+@\S+', x)
print(y)  # ['stephen.marquard@uct.ac.za']

# Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)', x)
print(y)  # [], x의 스트링이 'From'으로 시작하지 않으므로 해당되는 문자열이 없어 빈 리스트가 나옴. 그리고 괄호 안의 내용만 출력됨. From은 출력 X