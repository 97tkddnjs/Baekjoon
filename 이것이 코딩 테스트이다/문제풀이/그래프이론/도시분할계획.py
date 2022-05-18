# 백준 1647번
# 크루스칼 알고리즘
def find_parent(parent, x):
    
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a > b:
        parent[a] =b
    else:
        parent[b] =a

n, m = map(int, input().split())

parent = [0]*(n+1)
edges=[]

# 자기 자신으로 초기화를 해줌~
for i in range(1,n+1):
    parent[i] = i

for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b)) # 유지비 기준으로 정렬하도록

edges.sort() # 오름 차순 정렬이겠지
#print(edges)
result =[]

for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result.append(c)
        union_parent(parent,a,b) 
print(sum(result[:-1]))
#print(result)
