# 경쟁적 전염 BFS*
# 도저히 머리가 안돌아감... 
# 답지 보고 공부할 것 아 초기 아이디어 맞네? ㄹㅇ ㅋㅋㅋㅋㅋㅋㅋㅋ
# 일단 바이러스 위치를 저장하고 보는 것였다 답지 첫 줄 보고 확인함
import sys
from collections import deque

test=[]

n,k=map(int,sys.stdin.readline().split())
pos=[]

# 초기 설정하는 부분임
for i in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))

    for idx ,data in enumerate(tmp):
        if data !=0:
            # 얻은 힌트 굉장히 큰 힌트(바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            # 바이러스 + 위치 정도만 처음에 생각했다~
            pos.append((data, 0 ,i,idx))
    test.append(tmp)

s,rx,ry =map(int,sys.stdin.readline().split())

# 그 뭐냐 data 기준으로 일단 정렬~
pos.sort()

# 상 하 좌 우 
dx=[-1,1,0,0] # 행
dy=[0,0,-1,1] # 열

queue= deque(pos)

while queue:
    kind, sec, x, y = queue.popleft()

    if sec == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        #print(nx,ny)
        if test[nx][ny] == 0:
            test[nx][ny] = kind
            queue.append((kind,sec+1,nx, ny))

# for i in range(n):
#     for j in range(n):
#         print(test[i][j] ,end=" ")
#     print()


print(test[rx-1][ry-1])

'''
얻은 교훈 기본이 중요하다...
'''