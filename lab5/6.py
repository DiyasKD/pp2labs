import re
def f(s):
    return re.sub(r'[ ,.]', ':', s)

s = str(input())
print(f(s))
