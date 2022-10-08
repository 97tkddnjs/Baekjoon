
# 플로이드 워샬로 풀이해보기 <- 존나 하드 못함 이거~ ^^
# 다익스트라 알고리즘으로 풀어보겠어요

INF =int(1e9)
n = int(input())


# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


table= []

distance=[[INF]*n for i in range(n)]


for _ in range(n):
    table.append(list(map(int, input().split())))



for y in range(n):
    for x in range(n):
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>=n or ny<0 or ny>=n:
                continue




# for _ in range(n):
#     tmp=map(int, input().split())





# print(graph)