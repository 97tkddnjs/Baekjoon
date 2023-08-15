import sys
from collections import deque

input = sys.stdin.readline

# d 0 북 , 1 동 , 2 남 , 3 서
# graph 값이 0이면 청소되지 않은 칸
# 1 이면 벽

# 현재 체크
# 4칸 확인 다 청소 -> 후진 가능하면 후진 / 벽 멈춤(*)
# 청소되지 않은 칸이 있는 경우 -> 반시계



# 북 동 남 서
dx =[0 ,1 , 0, -1]
dy =[-1, 0 ,1 , 0]

direction =deque([0, 1, 2, 3])

N,M = map(int, input().split())
r, c, d = map(int, input().split())


while True:
    if direction[0]==d:
        break
    else:
        direction.rotate(1)


graph=[]

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)


cnt =0

while True:

    if graph[r][c] == 0:
        cnt+=1
        graph[r][c] = 2

    
    all_clean = False
    tmp = 0 
    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]
        if graph[ny][nx] == 2 or graph[ny][nx] == 1:
            tmp+=1
    
    if tmp==4:
        all_clean= True
    

    # 주변 4칸이 다 청소된 경우
    if all_clean:

        # 뒤 쪽 칸으로 갈 수 있는 지 판단
        back_dir = direction[2]

        nx = c + dx[back_dir]
        ny = r + dy[back_dir]

        if graph[ny][nx] == 1:
            break
        else:
            r= ny
            c= nx


    # 주변 4칸 중 청소되지 않은 경우가 있는 경우
    else:
        direction.rotate(1)
        front = direction[0]
        

        # 앞을 바라 봣을 때 청소 x 면 감
        nx = c + dx[front]
        ny = r + dy[front]

        if graph[ny][nx] == 0:
            r= ny
            c= nx

        pass
        

print(cnt)

#   북 동 남 서
#d = deque([0, 1, 2, 3])
# deque  rotate는 음수 넣음 왼쪽 양수 오른쪽임

#d.rotate(1)
#front = d[0]

