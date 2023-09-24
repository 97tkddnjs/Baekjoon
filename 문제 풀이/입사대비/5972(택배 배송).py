import sys
import heapq
INF = 1e9

input = sys.stdin.readline


n, m = map(int, input().split())


graph=[[] for _ in range(n+1)] 


visited=[0]*(n+1)
distance = [INF]*(n+1) 


for _ in range(m):
    a, b, c =map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))



def dijkstar(start):

    distance[start] = 0

    q= []
    heapq.heappush(q,(0,start))

    while q:
        dist , pos = heapq.heappop(q)    
        
        if distance[pos] < dist:
            continue

        for i in graph[pos]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstar(1)

print(distance[-1])


