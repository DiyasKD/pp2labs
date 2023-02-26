import re
def f(s):
    return re.findall('[A-Z][^A-Z]*', s)

s = str(input())
print(f(s))
