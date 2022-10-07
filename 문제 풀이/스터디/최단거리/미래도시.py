import sys

INF = int(1e9)
n, m = map(int ,input().split())

table = [[INF]*(n+1) for i in range(n+1)]



for a in range(n+1):
    for b in range(n+1):
        if a==b:
            table[a][b] =0

for i in range(m):
    a, b = map(int ,input().split())
    table[a][b]=1
    table[b][a]=1

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            table[a][b] = min(table[a][b], table[a][k]+table[k][b])

x, k = map(int ,input().split())

for a in range(n+1):
    for b in range(n+1):
        if table[a][b] == INF:
            print("x",end=" ")
        else:
            print(table[a][b],end=" ")
    print()