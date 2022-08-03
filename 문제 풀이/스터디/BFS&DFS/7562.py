from collections import deque
import sys


input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def bfs(a,b, n, aim_x,aim_y ,maps):

    queue= deque()
    queue.append((a,b))
    while queue:
        
        x, y = queue.popleft()
        if x ==aim_x and y == aim_y:
            return maps[x][y]
        
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            #print(nx,ny)
            if maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])

                
        pass



T = int(input())

for t in range(T):
        l = int(input())
        maps =[[0]*(l) for _ in range(l)]
        in_x, in_y = map(int, input().split())
        out_x, out_y = map(int,input().split())
        print(bfs(in_x,in_y, l, out_x,out_y ,maps))

