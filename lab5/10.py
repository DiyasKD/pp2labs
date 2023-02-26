import re
def f(s):
    ans = re.sub('(?<!^)(?=[A-Z])', '_', s).lower()
    return ans

s = str(input())
print(f(s))
