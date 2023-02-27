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