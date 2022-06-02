import sys
def binary_search(start, end,aim):
    
    global tree

    while(start<=end):
        mid = (start+end)//2
        k=check(mid,tree)
        if  k== aim:
            return mid
        elif k > aim:
            start= mid+1
        else:
            end =mid-1

    return end

def check(n,arr):
    global max
    global min
    sum_a=0
    for a in arr:
        if a>=n:
            sum_a+=(a-n)
    return sum_a

n,m = map(int,input().split())

tree =list(map(int,sys.stdin.readline().split()))

max=max(tree)

print(binary_search(1,max,m))