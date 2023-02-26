import re

def f(s):
    return re.findall(r'[A-Z][a-z]+', s)

s = str(input())
print(f(s))
