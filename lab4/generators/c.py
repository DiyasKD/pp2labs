n = int(input())
a = [i for i in range(n+1)]
b = [i for i in a if i % 3 == 0 and i % 4 == 0]
print(b)
