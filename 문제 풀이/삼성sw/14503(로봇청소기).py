import sys
from collections import deque

input =sys.stdin.readline

n, m = map(int, input().split())

# 반시계 방향으로
# 북 동 남 서
# 0  1  2 3

dir = deque([0,1,2,3])

# 북 동 남 서
dx=[0 ,-1, 0, 1 ] #  c
dy=[-1, 0, 1, 0]  # r

def algo(x,y, look):
    
    
    for i in range(4):
        
        if  y < 0 or y >= n or x<0 or x >= m:
            continue
        
        if data[y][x] == 0:
            pass


r, c ,d = map(int, input().split())
dir.rotate(d)

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


print(data, dir)


