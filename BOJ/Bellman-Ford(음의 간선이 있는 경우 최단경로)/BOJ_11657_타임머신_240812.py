v, e = list(map(int, input().split()))
# data = [
#     [1, 2, 4],
#     [1, 3, 3],
#     [2, 3, -4],
#     [3, 1, -2]
# ]
data = [ list(map(int, input().split())) for _ in range(e)]
inf = int(1e9)
distance = [inf] * (v+1)
start = 1
graph = [ [ ] for _ in range(v + 1)]
for s, e, c in data:
    graph[s].append((c, e))
# print(graph)
flag = True
distance[start] = 0

for s in range(v-1):
    for e in graph[s]:
        if distance[s] + e[0] < distance[e[1]]:
            distance[e[1]] = distance[s] + e[0]

for s in range(v):
    for e in graph[s]:
        if distance[s] + e[0] < distance[e[1]]:
            print(-1)
            flag = False
            break
    if not flag:
        break
else:
    for d in distance[2:]:
        print(d)  