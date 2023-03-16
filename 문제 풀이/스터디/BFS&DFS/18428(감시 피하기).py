import sys
from itertools import combinations
from collections import deque
import copy


input = sys.stdin.readline

size = int(input())

data = []
teacher = []
blank=[]

# 상 하 좌 우
dx = [0 , 0 , -1 , 1]
dy = [1, -1 , 0 , 0 ]

# 선생님 위치들 찾아서 -> bfs
# 그리고 빈공백에서 random 하게 3개
# -> for 문 돌리기




# search for teacher
def bfs(pos : tuple, data : list) -> bool : 
    queue = deque([pos])
    
    while queue:

        x, y = queue.popleft()
        
        for i in range(4):
            

            if data[x][y] ==  'O':
                return False


        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <=0 or nx >= size or ny <=0 or ny >= size:
                continue

            if data[nx][ny] == 'O':
                return False # 오 못찾겠어~
            
            if data[nx][ny] == 'S':
                print(data, (x,y), nx, ny)
                return True # 오 찾았어~
            

            if data[nx][ny] == 'X':
                data[nx][ny]='T'
                queue.append([nx,ny])
            
    return False

            

# data 정리도 함 해주고~
for _ in range(size):
    tmp = input().split()
    for i, val in enumerate(tmp):
        if val == 'T':
            teacher.append((_, i))
        if val == 'X':
            blank.append((_,i))
        

    data.append(tmp)


# 경우의 수 만들어 주고
blank_pos_comb = list(combinations(blank,3))

del blank


ans ='YES'
for blank_pos in blank_pos_comb:
    
    copy_data = copy.deepcopy(data)

    for i in blank_pos:
        c_x , c_y = i
        copy_data[c_x][c_y] = 'O'
    
    for t in teacher:
       if bfs(t, copy_data) :
            ans='NO'
            break

print(ans)




## <- 제일 간결했던 코드...
n = int(input())
graph = []
teacher = []
blank = []
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
for i in range(n):
  graph.append(list(input().split()))
  for j in range(n):
    if graph[i][j] == 'T':
      teacher.append((i, j))
    elif graph[i][j] == "X":
      blank.append((i, j))
 
def bfs(): # 학생 찾으면 False 반환
  q = deque(teacher)
  test_graph = copy.deepcopy(graph)
  while q:
    x, y = q.popleft()
    for i in range(4):
      temp_x, temp_y = x, y
      while True:
        nx = temp_x + dx[i]
        ny = temp_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
          if test_graph[nx][ny] == 'X':
            test_graph[nx][ny] = 'T'
          elif test_graph[nx][ny] == 'S':
            return False
          elif test_graph[nx][ny] == 'O':
            break
          temp_x, temp_y = nx, ny
        else:
          break
  return True
 
check = False
for data in list(combinations(blank, 3)):
  for x, y in data:
    graph[x][y] = 'O'
  if bfs():
    check = True
    break
  for x, y in data:
    graph[x][y] = 'X'
    
if check:
  print("YES")
else:
  print("NO")