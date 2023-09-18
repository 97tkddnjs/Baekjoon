import sys

input= sys.stdin.readline

n = int(input())

data= list(map(int, input().split()))

stack = []
last_idx = n-1
result = [0]*(n+1)

for i in range(n,-1 ,-1):
    while stack and data[i-1] > stack[-1][1]:
        pos , val = stack.pop()
        result[pos] = i

        
    # position , data 
    stack.append((i, data[i-1] ))

# print(result)
for i in range(1,n+1):
    print(result[i], end=" ")