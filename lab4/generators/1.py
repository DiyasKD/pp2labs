def sq(N):
    for i in range(N+1):
        yield i**2

n = int(input())
for i in sq(n):
    print(i, end=' ')
