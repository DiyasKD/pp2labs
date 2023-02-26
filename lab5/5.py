import re
s = 'a.*b$'

text = str(input())
if re.search(s, text):
    print("YEAH")
else:
    print("NO")
