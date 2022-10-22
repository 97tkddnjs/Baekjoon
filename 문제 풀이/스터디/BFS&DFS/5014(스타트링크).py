from collections import deque
import sys
input =sys.stdin.readline

# 총 f층 회사 G층 현재 s
# input
# F S G U D


F, S, G, U, D = map(int,input().split())

#visited=[False]



way =[U,-D]
# print(way)
graph =[0]*(F+1)


def bfs(start):
    queue = deque()
    
    queue.append(start)
    graph[start]=1 #########<- 이부분도,,,,

    while queue:
        

        pos =queue.popleft()
        # print("pos ",pos,queue)
        if graph[G] !=0:
            return graph[G]

        for i in range(2):
            npos = pos+ way[i]
            # print("npos ",npos)
            if npos<1 or npos > F:
                continue

            #BFS로 하기 때문에 이미 방문한 층에 한번 더 들르면 큰값이 들어가게 되므로 무조건 손해이다.
            # <- 최소 최대 조건 만족하려면 이것을 기억하는 게....
            if graph[npos]==0: ########### <- 내가 체크 하지 못한 부분
                graph[npos] = graph[pos]+1
                # print(graph)
                queue.append(npos)

data =bfs(S)
# <-- 출력 상황 역시 신경써야 하는 부분임
# 출발 지점 = 도착지점(목표지점)
if S == G:
	print(0)
    
# 출발지점 != 도착지점(목표지점)
else:
    # g층에 갈 수 없는 경우
	if graph[G] == 0:
		print("use the stairs")
    # g층에 갈 수 있는 경우
	else:
		print(graph[G]-1)
