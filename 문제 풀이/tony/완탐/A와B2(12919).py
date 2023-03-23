from itertools import product
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def func1( S : str) -> str:
    return (S+"A")
    

def func2(S : str) -> str:
    return (S+"B")[::-1]

def checkf(li):
    global S

    tmp_s = S
    for i in li:
        tmp_s = func1(tmp_s) if i == 0 else func2(tmp_s)
    return tmp_s

def dfs(idx, level):
    
    global S
    global T
    global check

    if idx == level:
        if checkf(result) == T:
            print(1)
            sys.exit()
        
        return
        
    for i in range(2):
        result[idx] = elem[i]
        checked[i] = True
        dfs(idx+1, level)
        checked[i]= False


elem = [0,1]


S = input().split()[0]
T =  input().split()[0]
 

check = False
length = len(T) - len(S)
result = [0]*length
checked =[False]*2

dfs(0, length)


print(0)


    
