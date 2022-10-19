import sys

input = sys.stdin.readline

n,m = map(int,input().split())

data=list(map(int,input().split()))
prefix_sum=[0]
sum_val = 0
for i in data:
    sum_val+=i
    prefix_sum.append(sum_val)

for i in range(m):
    start, end = map(int,input().split())
    print(prefix_sum[end]-prefix_sum[start-1])
