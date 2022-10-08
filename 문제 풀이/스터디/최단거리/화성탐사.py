
# 플로이드 워샬로 풀이해보기

INF =int(1e9)
n = int(input())

size= n*n


dx =[ ]

graph =[[INF]*(size+1) for _ in range(size+1)]

for a in range(size+1):
    for b in range(size+1):
        if a==b:
            graph[a][b]=0

# for _ in range(n):
#     tmp=map(int, input().split())

table= []

for _ in range(n):
    table.append(list(map(int, input().split())))

# print(graph)