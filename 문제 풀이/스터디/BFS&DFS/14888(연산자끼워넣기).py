import sys
from itertools import permutations, product
# 경우의수 안쓰고 풀기! 도전
input= sys.stdin.readline

n= int(input())
num =  list(map(int, input().split()))
op = []

for data, i in enumerate(list(map(int, input().split()))):
    if data==0:
        op.extend([0]*i)
    elif data==1:
        op.extend([1]*i)
    elif data==2:
        op.extend([2]*i)
    elif data==3:
        op.extend([3]*i)

# print(op)

operators = list(permutations(op,n-1))

# print(operators)
# operators =[(0, 0, 3, 1, 2),(1,3,0,0,2)]
res_min =1e9
res_max =-1e9

for ops in operators:
    tmp=num[0]
    
    for i, j in zip(num[1:],ops):
        # print(i,j)
        if j==0:
            tmp+=i
            # print("+",i,"=",tmp)
        elif j==1:
            tmp-=i
            # print("-",i,"=",tmp)
        elif j==2:
            tmp*=i
            # print("*",i,"=",tmp)
        elif j==3:
            tmp= int(tmp/i)
            
            # print("/",i,"=",tmp)
    # print("r tmp",res_min,tmp)
    res_min = min(res_min, tmp)
    res_max = max(res_max,tmp)
    # print("res_min",res_min)
            


print(res_max, res_min,sep="\n")
# (0, 0, 3, 1, 2)

# data = [0,0,1,2,3]
# a=list(product(data,repeat=5))

# print(a)