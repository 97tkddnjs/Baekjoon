# import sys

# 경우의 수로 먼저 풀오보겠으요 

from collections import deque
from copy import deepcopy
from itertools import combinations, permutations ,product

# 해당 문제에서의 그 좌표 전체의 값~
# data = [i for i in range(8)]
# all_xy = list(product(data ,repeat=2))
# print(all_xy)
# print(all_xy.count((0,0)))

# c =list(combinations(all_xy,3))
# print(len(c), c)


# virus 총 개수 반환
def virus(tmp_lab ,pos_data):
    # 상,하,좌,우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    count=len(pos_data)
    
    global n # 행, y축
    global m # 열, x축

    queue = deque()
    for p in pos_data:
        queue.append(p)
    while queue:
        
        x,y=queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_lab[nx][ny]==0:
                
                tmp_lab[nx][ny]=2
                count+=1
                queue.append((nx,ny))


    # print(tmp_lab,count)
    return count




n, m=map(int, input().split())

lab=[]
virus_xy_pos =[]
wall_pos =[]

zero_pos =[]
for row in range(n):
    tmp =list(map(int,input().split()))
    
    for col, data in enumerate(tmp):
        if data==2:
            virus_xy_pos.append((row , col))
        elif data==1:
            wall_pos.append((row , col))
        else:
            zero_pos.append((row , col))
    lab.append(tmp)


# print(zero_pos, virus_xy_pos)

# 경우의 수 <- 3가지 설치이니까

cmp = 0
cnt = n*m - len(wall_pos) -3
for comb in combinations(zero_pos,3):
    
    tmp = deepcopy(lab)
    for c in comb:
        t_x, t_y = c
        tmp[t_x][t_y]=1
    # print(tmp)
    # print(virus(tmp,virus_xy_pos))
    cmp = max(cmp, (cnt-virus(tmp,virus_xy_pos)))
    
    # print(cmp)
    pass
    
print(cmp)


