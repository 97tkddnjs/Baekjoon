import sys

test=[]

n,k=map(int,sys.stdin.readline().split())
pos=[ [] for i in range(k+1) ]

for i in range(n):
    tmp=map(int,sys.stdin.readline().split())
    for idx,j in enumerate(tmp):
        if j !=0: # x,y , 행. 렬
            pos[j].append([i, idx] )

    test.append(tmp)

s,x,y =map(int,sys.stdin.readline().split())

# 상 하 좌 우 
dx=[-1,1,0,0] # 행
dy=[0,0,-1,1] # 열

def move(position,num):
    
    for i in range(4):
        nx=position[0]+dx
        ny=position[1]+dy

        if nx<0 and nx >=n and ny<0 and ny>=n:
            pass
        else:
            test[nx][ny] =num


print(test[x-1][y-1])