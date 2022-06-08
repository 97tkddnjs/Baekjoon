# 특정 거리의 도시 찾기

from collections import deque
import sys

n,m,k,x = map(int,sys.stdin.readline().split())
Inf=300000
visited=[False]*(n+1)
length=[Inf]*(n+1)
dist=[[] for i in range(n+1)]

# for i in range(m): # 출력 초과 이유 양방향 그래프를 만든것이다~
#     a,b= map(int,sys.stdin.readline().split())
#     dist[a].append(b)
#     dist[b].append(a)

for i in range(m): # 맞는 코드!
    a,b= map(int,sys.stdin.readline().split())
    dist[a].append(b)



def bfs(init):

    queue= deque([init])
    visited[init]=True
    length[init]=0

    while queue:
        v= queue.popleft()
        for i in sorted(set(dist[v])):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                length[i]=length[v]+1 # 핵심임 시작에서 +1이 되는 것이니까~


bfs(x)
check= False

for idx, res in enumerate(length):
    if res == k:
        print(idx)
        check=True

if check == False:
    print(-1)