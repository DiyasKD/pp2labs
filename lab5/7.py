import re

def f(s):
    return re.sub(r'_(.)', lambda m: m.group(1).upper(), s)

s = str(input())
print(f(s))
