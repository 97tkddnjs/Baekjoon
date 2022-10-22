from collections import deque
import sys
input =sys.stdin.readline

# 총 f층 회사 G층 현재 s
# input
# F S G U D


F, S, G, U, D = map(int,input().split())

#visited=[False]



way =[U,-D]
print(way)
graph =[0]*(F+1)


def bfs(start):
    queue = deque()
    
    queue.append(start)

    while queue:
        

        pos =queue.popleft()
        # print("pos ",pos)
        if graph[G] !=0:
            return

        for i in range(2):
            npos = pos+ way[i]
            # print("npos ",npos)
            if npos<1 or npos > F:
                continue

            graph[npos] = graph[pos]+1
            print(graph)
            queue.append(npos)


print(bfs(S))
print(graph) 