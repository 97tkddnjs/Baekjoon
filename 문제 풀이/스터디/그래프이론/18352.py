from collections import deque
import sys

n,m,k,x = map(int,sys.stdin.readline().split())
Inf=300000
visited=[False]*(n+1)
length=[Inf]*(n+1)
dist=[[] for i in range(n+1)]

for i in range(m):
    a,b= map(int,sys.stdin.readline().split())
    dist[a].append(b)
    dist[b].append(a)



cnt=0
result=[]

def bfs(init, key):

    queue= deque([init])
    visited[init]=True
    length[init]=0
    cnt=1
    while queue:
        v= queue.popleft()
        for i in sorted(set(dist[v])):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                length[i]=length[v]+1
                if length[i]==key:
                    result.append(i)
        cnt+=1

bfs(x,k)
#print(length)
if result:
    for i in result:
        print(i)
else:
    print(-1)