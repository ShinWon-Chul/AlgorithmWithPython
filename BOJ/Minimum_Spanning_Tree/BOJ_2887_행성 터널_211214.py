def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
loads = []
for _ in range(n):
    loads.append(list(map(int, input().split())))
    
x = []
y = []
z = []
for i, v in enumerate(loads):
    x.append((v[0], i+1))
    y.append((v[1], i+1))
    z.append((v[2], i+1))
    
x.sort()
y.sort()
z.sort()
edges = []
for i in range(n-1):
    edges.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    edges.append((abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))
    
edges.sort()

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

costs = []
for cost, a, b, in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        costs.append(cost)
print(sum(costs))