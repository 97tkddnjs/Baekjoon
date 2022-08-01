import heapq
import sys
input = sys.stdin.readline
INF = (1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int,input().split())

#시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph=[[] for i in range(n+1)]
distance =[INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 C
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    