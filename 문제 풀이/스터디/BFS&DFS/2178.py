from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph=[]

for i in range(n):
    tmp =input().split()
    print(tmp.split(''))
    graph.append(tmp)


print(graph)
