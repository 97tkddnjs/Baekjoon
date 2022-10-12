

from collections import deque


test = int(input())

for _ in range(test):
    v, e = map(int, input().split())

    visited = [False]*(v+1)
    
    color = [0]*(v+1)
    print(color)
    graph= [[] for _ in range(v+1)]
    print(graph)
    for i in range(e):
        a,b=map(int, input().split())
        graph[a].append(b)
    
    queue = deque()
    queue.append([1])
    visited[1] = True
    color[1] = 1
    while queue:
        x = queue.popleft()
        c = color[x]

        for i in graph[x]:
            if color[i] !=0 and c == color[i]:
                print("NO")
                break                
            if not visited[i]:
                visited[i]= True
                queue.append(i)
                color[i] = -c  

    print("YES")
