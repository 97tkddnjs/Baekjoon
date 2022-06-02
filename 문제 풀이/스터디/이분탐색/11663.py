import sys

def binary_search(start, end,aim):
    global arr

    while(start<=end):
        mid = (start+end)//2

        if  arr[mid]== aim:
            return mid
        elif  arr[mid] < aim:
            start= mid+1
        else:
            end =mid-1

    return  end


n,m = map(int,input().split())

arr =list(map(int,sys.stdin.readline().split()))
arr.sort()
length = n-1
for i in range(m):
    a, b =map(int,input().split())
    check_a=binary_search(0,length,a)
    check_b=binary_search(0,length,b)
    
    ans=0
    
    if arr[check_a] <a:
       pass
    else:
        ans+=1
    
    if arr[check_b] <=b:
       pass
    else:
        ans-=1
    
    ans+=(check_b-check_a)+1
    print(ans)
    