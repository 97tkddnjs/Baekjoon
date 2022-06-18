# 적록 색약
import copy
import sys
sys.setrecursionlimit(10000)
n= int(input())
arr=[]
# RGB
result =[0,0,0]
result_diff=0
# x -> row , y->col


def dfs(x,y,string,arr,diff=False):

    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if diff == False:
        if arr[x][y]==string:
            arr[x][y] = 0
            dfs(x-1,y,string,arr,diff)
            dfs(x,y-1,string,arr,diff)
            dfs(x+1,y,string,arr,diff)
            dfs(x,y+1,string,arr,diff)
            return True

    else:
        if arr[x][y]=='R' or arr[x][y]=='G':
            arr[x][y] = 0
            dfs(x-1,y,string, arr,diff)
            dfs(x,y-1,string, arr,diff)
            dfs(x+1,y,string, arr,diff)
            dfs(x,y+1,string, arr,diff)
            return True
        
    return False

for i in range(n):
    arr.append(list(input()))

arr_copy= copy.deepcopy(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] =='R' or arr[i][j] =='G':
            
            if arr[i][j] =='R':
                if dfs(i,j,'R',arr):
                    result[0]+=1
            elif arr[i][j] =='G':
                if dfs(i,j,'G',arr):
                    result[1]+=1

            if dfs(i,j,arr_copy[i][j],arr_copy,True):
                result_diff+=1
        
        elif arr[i][j] =='B':
            if dfs(i,j,'B',arr):
                result[2]+=1


print(sum(result), result_diff+result[2],sep=" ")