import re

def f(s):
    return re.findall(r'[a-z]+(?:_[a-z]+)+', s)

s = str(input())
print(f(s))
