import heapq
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a].append((dist, b))
    graph[b].append((dist, a))
v1, v2 = map(int, input().split())

inf = int(10e9)
start = 1
h = []
def dijkstra(start):
    
    heapq.heappush(h, (0, start))
    distance = [inf] * (n+1)
    distance[start] = 0
    while h:
        dist, node = heapq.heappop(h)
        if distance[node] < dist:
            continue
        else:
            for next_node in graph[node]:
                d = dist + next_node[0]
                if distance[next_node[1]] > d:
                    distance[next_node[1]] = d
                heapq.heappush(h, (d, next_node[1]))
    return distance

start_distance = dijkstra(start)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

path1 = start_distance[v1]+v1_distance[v2]+v2_distance[n]
path2 = start_distance[v2]+v2_distance[v1]+v1_distance[n]

result = min(path1, path2)
if result >= inf:
    print(-1)
else:
    print(result)