import re
text = str(input())
s = 'a(b*)'
if re.search(s,  text):
        print("YEAH")
else:
        print("NO")
