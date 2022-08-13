from collections import deque
import sys
input = sys.stdin.readline


n, m, r = map(int, input().split())
graph=[ [] for i in range(n+1) ]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    pass

visited=[0]*(n+1)
data=[]

cnt=1


def bfs(start):
    
    global cnt

    queue= deque()

    queue.append(start)
    visited[start]=cnt
    cnt+=1
    while queue:

        x= queue.popleft()
        # print(x)    
        data.append(x)
        for i in sorted(graph[x]):
            
            if  visited[i] == 0:
                # print("i ",i ," ",cnt) 
                visited[i] = cnt
                queue.append(i)
                cnt+=1
            
bfs(r)

for i in visited[1:]:
    print(i)