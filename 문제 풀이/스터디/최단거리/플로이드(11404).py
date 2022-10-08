INF =int(1e9)

n =int(input())
m =int(input())


graph=[[INF]*(n+1) for i in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b]=min(c,graph[a][b]) # min을 쓰면 맞다고 한다... 확인해보니 같은 경로가 두 번 이나 있음

print("\n\n\n===================original")
for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print("x",end=" ")
        else:
           print(graph[a][b],end=" ")
    print()

for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print("\n\n\n===================after")
for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print("x",end=" ")
        else:
           print(graph[a][b],end=" ")
    print()