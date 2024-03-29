
def union_parent(parent, a, b):
    a= find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b] =a
    else:
        parent[a] =b

# 경로 압축 기법 소스코드
def find_parent(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# v : 노드의 개수 , e : 간선의 개수
v, e = map(int, input().split())
parent=[0]*(v+1)

# 부모 테이블상에서,부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] =i



cycle =False

for i in range(e):
    a,b = map(int,input().split())
    # 사이클이 발생하는 경우 종료를 한다.
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    #사이클이 발생하지 않은 경우 합집합을 수행한다.
    else:
        union_parent(parent,a,b)

if cycle:
    print("cycle True")
else:
    print("cycle False")