import sys
import heapq

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

graph =[]



first_idx=0

last_idx = len(data)-1


while first_idx < last_idx:
    
    mid_val = data[first_idx] +data[last_idx] 
    heapq.heappush(graph,(abs(mid_val), (data[first_idx] ,data[last_idx] ) ) )    
    if mid_val == 0:
        break
    elif mid_val > 0:
        last_idx-=1
    else:
        first_idx+=1

    pass



first, last =graph[0][1]
print(first, last)