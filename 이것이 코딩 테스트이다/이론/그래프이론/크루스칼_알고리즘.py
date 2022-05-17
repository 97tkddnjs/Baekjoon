
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
parent=[0]*(v+1) # cycle 체크를 위해서 필요할 수 밖에 없네

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서,부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] =i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
    pass

# 간선을 비용순으로 정렬하기
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b= edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result +=cost

print(result)