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

def algo(x,y , stop):
    
    check = False
    

    # 주변 4칸 체크
    for i in range(4):
        
        if  y < 0 or y >= n or x<0 or x >= m:
            continue
        ny = y + dy[i]
        nx = x + dx[i]
        if data[ny][nx] == 0:
            check =True
            break
    print(check)
    if check:
        dir.rotate(1)
        nx = x+dx[dir[0]]
        ny = y + dy[dir[0]]
        if data[ny][nx] == 0:
            x = nx
            y = ny
    else:
        dir.rotate(2)
        nx = x+dx[dir[0]]
        ny = y + dy[dir[0]]
        if data[ny][nx] == 0:
            x = nx
            y = ny
        else:
            stop =True
        dir.rotate(2) # 원복
    
    return ( x, y , stop)


r, c ,d = map(int, input().split())
dir.rotate(d)

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


print(data, dir)
stop =False
x = c
y = r
cnt = 0
s=set()
while not stop:
    x, y, stop = algo(x, y , stop)
    print(x,y, stop)
    s.add((y,x))
    cnt+=1
    if cnt >=100:
        break

print(s)
print(cnt)



