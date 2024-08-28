# Find the root node of x recursively.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union the two sets.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 크루스칼 알고리즘 가장 비용이 적은 간선을 우선 선택
edges.sort()

# Check in order of low-cost edges.
for edge in edges:
    cost, a, b = edge
    # If there will be no cycle, union.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)