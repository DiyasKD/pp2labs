def div_3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for i in div_3_4(n):
    print(i, end=' ')
