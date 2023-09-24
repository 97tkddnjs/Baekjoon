import sys
from collections import deque

'''
내가 푼 풀이 
문제점 지훈이랑 불을 동시에 이동하려고 함 이래서 문제였던 듯

해결책 

1. 불을 먼저 전부 이동 시키고
2. 이 후 나머지 지훈이를 이동시킨다. 

이렇게 풀면 해결...
월까지 마감하기 미션~~

'''

input = sys.stdin.readline

R, C =map(int, input().split())
min = 0
graph =[]

fire =deque()
jh =deque()

for r in range(R):
    tmp =list(input().rstrip())
    
    for c, t in enumerate(tmp):

        if t =='J':
            jh.append((r,c))
        elif t=='F':
            fire.append((r,c,min))
        

    graph.append(tmp)

del tmp



dx =[ 0 ,0 ,-1, 1]
dy =[-1, 1, 0, 0]

exit_flag =False

print(graph)
# print(jh)
while jh and exit_flag ==False:

    y, x = jh.popleft()
    min+=1
    # print(y," " ,x)
    #  jh move
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if graph[ny][nx]=='F':
            continue

        if ny < 0 or ny>=R or nx<0 or nx>=C:
            print(graph)
            exit_flag =True
            del fire
            # del jh
            break
        
        
        if graph[ny][nx]=='.':
            print("ny : nx  ", ny, nx)
            graph[ny][nx]='J'
           
            jh.append((ny,nx))
    
    # fire move

    if exit_flag==False:
        while fire:
            
            y , x , m= fire.popleft()
            if m ==min:
                break

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny>=R or nx<0 or nx>=C :
                    continue

                print("fff ny : nx  ", ny, nx)
                if graph[ny][nx]=='#':
                    continue

                graph[ny][nx] ='F'    
                fire.append((ny,nx,min))
if exit_flag:
    print(min)
else:
    print("IMPOSSIBLE")



