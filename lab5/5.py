import re
s = 'a.*b$'

ins = str(input())
if re.match(s, ins):
    print("YEAH")
else:
    print("NO")
