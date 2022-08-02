import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    global cnt
    print(v)

    # 오름차순 만들어주기
    graph[v].sort()
    for i in graph[v]:
        #print("i ",i, v ,visited[v])
        if not visited[i]:
            dfs(graph,i,visited)

n,m,r= map(int, input().split())

graph=[[] for _ in range(n+1) ]


cnt = 0

for i in range(m):
    x, y= map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#print(graph)
visited=[False]*(n+1)
dfs(graph, r, visited)
for data in range(n-cnt):
    print(0)