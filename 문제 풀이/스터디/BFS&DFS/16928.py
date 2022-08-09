# 뱀과 사다리 게임 <- 아이디어는 답지랑 비슷했으나... 뭔가 잘 안되네..... 흐음 무조건 풀어보기 다시
# 탐색 느낌이면 bfs dfs
# 다음으로 풀어볼 문제 
# https://www.acmicpc.net/problem/14226

# 기본 코드인데 안풀린 이유 <- 공부해둘 것!
# 조건이 나올 경우 조건을 그냥 다 해준다고 생각해보자!
# 
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
        
        if arr[nx]==0:
            if not snake.get(nx): # 뱀 위치가 아님
                if ladder.get(nx): # 사다리가 있다?
                    y = ladder[nx]
                    arr[y]=arr[nx]+1 # 이동하는 사다리 위치 +1
                    queue.append(y)

                queue.append(nx)
                arr[nx]+=cnt
    cnt+=1



print(arr)

# 16928 뱀과 사다리 게임

from collections import deque

# 사다리의 수, 뱀의 수 입력받기
n, m = map(int, input().split())

# 1부터 100번째 칸 방문횟수
board = [0] * 101
# 맵 방문표시
visited = [False] * 101

# 사다리, 뱀 딕셔너리 선언
ladder = dict()
snake = dict()
# 사다리 정보 입력받기
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
# 뱀 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b


# 큐 구현
q = deque([1])

# 큐가 빌 때까지 반복
while q:
    x = q.popleft()
    # 100번 칸에 도착했다면
    if x == 100:
        # 주사위 굴린 횟수 출력
        print(board[x])
        # 반복문 탈출
        break
    # 주사위에 있는 1부터 6까지 차례대로 입력받아
    for dice in range(1, 7):
        # 다음으로 이동할 위치 보기
        next_place = x + dice
        # 맵을 벗어나지 않거나 아직 방문하지 않은 칸이라면
        if next_place <= 100 and not visited[next_place]:
            # 이동할 위치에 사다리가 있다면
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            # 이동할 위치에 뱀이 있다면
            if next_place in snake.keys():
                next_place = snake[next_place]
            # 이동할 위치에 아무것도 없다면
            if not visited[next_place]:
                # 방문 표시
                visited[next_place] = True
                # 주사위 굴린 횟수 추가
                board[next_place] = board[x] + 1
                # 큐에 이동한 위치 삽입
                q.append(next_place)