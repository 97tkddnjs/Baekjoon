from collections import deque

import sys
input= sys.stdin.readline

array=[]

n, m = map(int,input().split())

for _ in range(n):
    array.append(list(map(int,input().rstrip())) )

print(array)

# 상 하 좌 우 
dx=[-1,1,0,0] # 행
dy=[0,0,-1,1] # 열

break_wall = True
queue = deque()
queue.append((0,0))
cnt=0

while queue:
    
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >=n or ny<0 or ny>=m:
            continue

        if array[nx][ny] == 0:
            queue.append((nx, ny))
            array[nx][ny]=array[x][y]+1

        else:
            if break_wall:
                queue.append((nx, ny))
                cnt+=1
                array[nx][ny]=array[x][y]+1
                break_wall =False


print(array,array[n-1][m-1])

