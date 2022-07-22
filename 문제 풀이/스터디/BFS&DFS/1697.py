# 숨바꼭질 문제 실버 1



from collections import deque
import queue


def bfs(x, target):
    
    queue = deque(x)
    
    cnt =0
    while queue:
        
        data = queue.popleft()
        x-1
        x+1
        x*2

        pass

    pass

n,m = map(int,input().split())


#https://www.acmicpc.net/board/view/82583

from collections import deque

N, K = map(int, input().split())
board = [0 for _ in range(200000)]

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()
    if x == K:
        break
    dx = [x - 1, x + 1, 2 * x]
    for i in dx:
        if 0 <= i < 200000 and not board[i]:
            board[i] = board[x] + 1
            queue.append(i)

print(board[K])
