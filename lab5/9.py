import re
def f(s):
    return re.sub(r'(?<=\w)([A-Z])', r' \1', s)

s = str(input())
print(f(s))
