def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
# 부모 테이블 생성
parent = [0] * (v+1)
# 부모 테이블의 각 노드의 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))
edges.sort(key = lambda x : x[-1])

result = 0
for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost
    else:
        continue
if v == 1:
    print(0)
else:
    print(result)