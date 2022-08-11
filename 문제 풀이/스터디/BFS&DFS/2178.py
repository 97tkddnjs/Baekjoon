from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int, input().rstrip())))


# print(graph)

queue=deque()
queue.append((0,0))

# 상하좌우
dx = [0, 0 ,-1, 1]
dy = [1, -1 ,0, 0]

while queue:

    data= queue.popleft()
    #print(data)
    x, y =data
    if y==n-1 and x== m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y+ dy[i]
        
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        if graph[ny][nx] == 1:
            queue.append((nx,ny))
            graph[ny][nx] = graph[y][x]+1
            pass
        

print(graph[n-1][m-1])