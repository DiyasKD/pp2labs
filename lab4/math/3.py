import math
n = float(input())
a = float(input())
p = n * a
s = a / (2*math.tan(math.pi / n))
print(p * s / 2)
