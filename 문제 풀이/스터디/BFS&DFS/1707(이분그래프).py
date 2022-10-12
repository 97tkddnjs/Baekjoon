

from collections import deque

def bfs(start ,data):
    queue = deque()
    queue.append(start)
    visited[start] = True
    color[start] = data
    #print(graph)
    #print(visited)
    #print(queue)
    while queue and res:
        x = queue.popleft()
        c = color[x]
        
        for i in sorted(graph[x]):
            if color[i] !=0 and c == color[i]:
                return False
                        
            if not visited[i]:
                visited[i]= True
                queue.append(i)
                color[i] = -c
    return True

test = int(input())

for _ in range(test):
    v, e = map(int, input().split())
    res=True
    visited = [False]*(v+1)
    color = [0]*(v+1)
    graph= [[] for _ in range(v+1)]
    
    for i in range(e):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    
    # 이걸로 완전 연결 그래프인지 체크했다...
    for i in range(1,v+1):
        if not visited[i]:
            res =  bfs(i,1)
            if not res:
                break
    print('YES' if res else 'NO')
    
    
