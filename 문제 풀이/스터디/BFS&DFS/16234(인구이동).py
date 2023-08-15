<<<<<<< HEAD
from collections import deque



dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited= set()

def bfs(visited, graph):
    queue = deque()
    queue.append((0,0))

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



def dfs(visited, graph):

    visited

    pass

=======
from collections import deque
import sys

input = sys.stdin.readline

N, L ,R = map(int, input().split())
# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0]*N for _ in range(N)]

data = []

for _ in range(N):
    data.append(list(map(int, input().split()))) 

# print( not 0)
def bfs():


    queue = deque()
    queue.append((0,0))
    cnt =1
    sum_num = data[0][0]
    visited[0][0] +=1

    while queue:
        
        y, x = queue.popleft()

        for i in range(4):

            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx>=N or ny<0 or ny>=N:
                continue
            
            
            tmp = abs(data[ny][nx] - data[y][x])
            print("tt  ",tmp , ny , nx , visited , visited[ny][nx], L<= tmp, tmp <=R)
            # 여긴 아주 새로 방문하는 상황
            if (L<= tmp and tmp <=R) and not visited[ny][nx]:
                
                visited[ny][nx] = 1
                queue.append((ny,nx))
                cnt+=1
                sum_num += data[ny][nx]
                print("tt1  ",tmp , ny , nx)

            # 그니까 마이너스 해서 같은 값인 것임
            if tmp == 0 and visited[ny][nx] != visited[y][x]:
                print("tt2  ",tmp , ny , nx)
                queue.append((ny,nx))
                visited[ny][nx] +=1
                pass

    print(sum_num, cnt, sum_num//cnt)           
    if cnt > 1:
        return sum_num//cnt
    
    return -1


def change(val):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                data[i][j] = val



move =0
val = 0

val = bfs()

while val !=-1:
    move+=1
    change(val)

    val = bfs()

print(move)
>>>>>>> 39a3a10a0f8a062647c4fcb52eb18206515745bf
