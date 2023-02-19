def sq(N):
    i = N
    while i >= 0:
        yield i
        i -= 1

n = int(input())
for i in sq(n):
    print(i, end=' ')
