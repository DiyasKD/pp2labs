import re
s = 'ab{2,3}'
text = str(input())
if re.search(s,  text):
        print("YEAH")
else:
        print("NO")
