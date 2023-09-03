import sys
input = sys.stdin.readline


n = int(input())

data= []

for _ in range(n):
    data.append(int(input()))

data.sort()


tmp_val = 0
if n >=2:
    tmp_val = data[0]+data[1]
else:
    tmp_val=0
sum_val = tmp_val

for i in range(2,n):
    tmp_val+=data[i]

    sum_val +=tmp_val

print(sum_val)