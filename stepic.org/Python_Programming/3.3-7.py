n = int(input())
X = [int(input()) for i in range(n)]
D = {}
for x in X:
    if x not in D:
        D[x] = f(x)
    print(D[x])