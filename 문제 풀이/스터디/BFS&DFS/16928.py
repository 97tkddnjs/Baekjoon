# 뱀과 사다리 게임 <- 아이디어는 답지랑 비슷했으나... 뭔가 잘 안되네..... 흐음 무조건 풀어보기 다시
# 탐색 느낌이면 bfs dfs

from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())


dx=[1,2,3,4,5,6]

arr=[0] * 101 # 전체 탐색을 위한 그래프

ladder = {}
snake={}

for i in range(n):
    x,y = map(int, input().split())
    ladder[x]=y
    

for i in range(m):
    x,y = map(int, input().split())
    snake[x]=y
    pass


queue= deque([1])
res=0
cnt=1
while queue:
    
    x = queue.popleft()
    # if arr[100] !=0:
    #     break

    for i in dx:
        nx= x+i
        # print(nx)
        if nx >=100:
            break
        
        if arr[nx]>=0:
            if not snake.get(nx): # 뱀 위치가 아님
                if ladder.get(nx): # 사다리가 있다?
                    y= ladder[nx]
                    arr[y]=arr[nx]+1 # 이동하는 사다리 위치 +1
                    queue.append(y)

                queue.append(nx)
                arr[nx]+=cnt
    cnt+=1



print(arr)

