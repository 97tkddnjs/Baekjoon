import sys
# sys.setrecursionlimit(10**6)

input = sys.stdin.readline

cnt = 0

cnt2=0 
n = int(input())
def fib(n):
    global cnt
    
    if n == 1 or n ==2:
        cnt+=1
        return 1
    else:
         return fib(n-1)+fib(n-2)


def fibonacci(n):
    cnt2=0
    f=[0,1,1]
    for i in range(3,n+1):
        f.append( f[i-1]+f[i-2])
        cnt2+=1
    return cnt2


fib(n)

print(cnt, fibonacci(n))