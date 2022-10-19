import sys

input = sys.stdin.readline

# 시간 초과 코드~
n, h= map(int, input().split())

size =n//2

height_arr= [0]*(h+1)
up =[]
bottom=[]


for i in range(size):
    
    tmp1=int(input())
    bottom.append(tmp1)
    
    tmp2= int(input())
    up.append(tmp2)

for i in range(size):
    bottom[i]
    up[i]
    pass
    

data = height_arr[1:].sort()
cnt=1
for i in data:
    if data[0]==i:
        cnt+=1
print(data[0],cnt)

