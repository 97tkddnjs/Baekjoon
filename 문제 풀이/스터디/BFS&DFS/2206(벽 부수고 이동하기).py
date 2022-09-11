from collections import deque
import queue
import sys
input= sys.stdin.readline

array=[]

n, m = map(int,input().split())

for _ in range(n):
    array.append(list(map(int,input().rstrip())) )

print(array)

queue = deque()

