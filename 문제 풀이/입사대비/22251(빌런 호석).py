import sys
input = sys.stdin.readline

number=[]

tmp = [0]*7

for i in range(10):
    tmp = [1]*7

    if i == 0:
        tmp[3]= 0
    if i == 1:
        tmp =[ 1 if i==2 or i==5 else 0 for i in range(10)]

    elif i == 2 :
        tmp[1] =0
        tmp[5] =0
    elif i == 3:
        tmp[1] = 0
        tmp[4] = 0
    elif i== 4:
        tmp[0] = 0
        tmp[4] = 0
        tmp[6] = 0
    elif i==5:
        tmp[2] = 0
        tmp[4] = 0
    elif i==6:
        tmp[2] == 0
    elif i==7:
        tmp =[ 1 if i==0 or i==2 or i==5 else 0 for i in range(10)]
    elif i==9:
        tmp[4] = 0

    number.append(tmp)

N,K,P,X = map(int, input().split())


data =[]

for k in range(K):
    idx = X%10
    X = X//10

    data.append(number[idx])
    