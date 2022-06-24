# 토마토
from collections import deque

m , n = map(int, input().split())

box=[]
pos=[]
queue= deque()

# 상 하 좌 우 
dx=[-1,1,0,0] # 행
dy=[0,0,-1,1] # 열
day=0

tot_cnt= m*n

for row ,_ in enumerate(range(n)):
    tmp =list(map(int, input().split()))

    for col ,find_num in enumerate(tmp):
        if find_num == 1:
            queue.append((day ,row,col))
            tot_cnt-=1

        elif find_num == -1:
            tot_cnt-=1

    box.append(tmp)


while queue:

    day ,x, y = queue.popleft()

    day+=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx>= n or ny<0 or ny>=m:
            continue

        if box[nx][ny]==0:            
            queue.append((day,nx,ny))
            box[nx][ny]=1
            tot_cnt-=1        

if tot_cnt == 0:
    print(day-1)
else:
    print(-1)