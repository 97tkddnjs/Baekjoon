import sys

input = sys.stdin.readline()

r, c = map(int,input().split())

graph=[]

for _ in range(r):
    tmp = list(input().split())
    graph.append(tmp)

print(graph)

def bfs():
    pass



