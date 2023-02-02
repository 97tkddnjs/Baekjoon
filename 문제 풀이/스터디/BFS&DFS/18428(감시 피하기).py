import sys
from itertools import combinations

input = sys.stdin.readline

size = int(input())

data = []
teacher = []
blank=[]

# 선생님 위치들 찾아서 -> bfs
# 그리고 빈공백에서 random 하게 3개
# -> for 문 돌리기

for _ in range(size):
    tmp = input().split()
    data.append(tmp)


print(data)

