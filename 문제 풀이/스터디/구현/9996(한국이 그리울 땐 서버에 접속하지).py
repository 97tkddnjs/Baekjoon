import sys

input =sys.stdin.readline

n= int(input())

st = input()
# print(st)
data =st[:-1].split("*")

init_d = data[0]
last_d = data[1]

# print(data)
for i in range(n):

    tmp = input()
    if len(data)<len(tmp):
        # 슬라이싱을 하게 되면 만약 지정한 크기 만큼 없다고 해도 오류를 내는 것이 아닌 마지막 문자를 돌려줌
        # 따라서 아래와 같은 로직을 했어야 된다...
        if tmp[:len(init_d)] == init_d and tmp[-len(last_d)-1:-1] ==last_d:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")
    pass

# 정답 코드
test=int(input())
ref=list(input())
star=ref.index('*')
r=[]
r.append(ref[:star])
r.append(ref[(star+1):])#*기준으로 왼쪽 오른쪽 분리

for i in range(test):
    x=0
    tar=list(input())
    if len(r[0])<=len(tar):#왼쪽비교
        if r[0]==tar[:len(r[0])]:
            x=x+1
        tar=tar[len(r[0]):]#중복제거를위함
    if len(r[1])<=len(tar):#오른쪽비교
        if r[1]==tar[-len(r[1]):]:
            x=x+1
    if x==2:
        print('DA')
    else:
        print('NE')