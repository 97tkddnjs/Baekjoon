from collections import deque
import time
import copy
def solution(grid, k):
    
    n =len(grid)
    m = len(grid[0])

    grid = list(map(list,grid))

    visited= [[0]*m for i in range(m) ]#copy.copy(grid)

    queue = deque()
    queue.append((0,0))
    

    dx =[-1,1,0,0]
    dy= [0,0,-1,1]
    
    cnt=0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if nx<0 or ny <0 or nx>=n or ny>=m:
                continue
            # water
            if grid[nx][ny] =='#':
                continue

            #print(grid[nx][ny])
            if grid[nx][ny] =='.' or grid[nx][ny] =='F':
                cnt+=1
                grid[x][y] ='#'
                visited[nx][ny] = visited[x][y]+1
                print(nx, ny)

                for data in visited:
                    for i in data:
                        print(i,end=" ")
                    print()
                print()
                queue.append((nx,ny))
                
            
    
    print(visited)
            


    answer = cnt
    return answer



solution(["..FF", "###F", "###."], 4)
solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)