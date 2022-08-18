from collections import deque
import sys

input = sys.stdin.readline

m,n,h= map(int,input().split())

# 상 하 좌 우 위 아래

dx=[-1,1,0,0,0,0] # 행
dy=[0,0,-1,1,0,0] # 열
dz=[0,0,0,0,1,-1] # z

baket=[]

# m - x
#n -y
tot_one=0
tot_minus=0
day=0

queue = deque()

sorted()
for dim in range(h):
    tmp=[]
    for row in range(n):
        tmp1=list(map(int,input().split()))
        tmp1.sort(reverse=True)
        for col,data in enumerate(tmp1):
            if data==1:
                tot_one+=1
                queue.append((dim,row,col,day))
            elif data ==-1:
                tot_minus+=1

        tmp.append(tmp1)
    baket.append(tmp)

tot_cnt = (m*n*h) -(tot_minus+tot_one)

while queue:
    
    z,y,x ,tmp_day= queue.popleft()
    tmp_day+=1
    day=tmp_day
    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]

        if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
            continue
        
        if baket[nz][ny][nx]==0:
            
            baket[nz][ny][nx] =1
            tot_cnt-=1
            queue.append((nz,ny,nx,tmp_day))
            pass

if tot_cnt !=0:
    print(-1)
else:
    print(day-1)