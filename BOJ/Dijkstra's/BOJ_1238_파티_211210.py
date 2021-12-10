import heapq
inf = int(1e9)
v, e, start = list(map(int, input().rstrip().split()))
distance = [inf] * (v+1)
distance[start] = 0

graph = [[] for _ in range(v+1)]
for _ in range(e):
    s,e,d = list(map(int, input().rstrip().split()))
    graph[s].append((d,e))

h = []
def Dijcstra(start):
    heapq.heappush(h, (0, start))
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(h, (cost, i[1]))
                
Dijcstra(start)
totalDistance = distance

for i in range(1, v+1):
    if i != start:
        distance = [inf] * (v+1)
        distance[i] = 0
        Dijcstra(i)
        totalDistance[i] += distance[start]
print(max(totalDistance[1:]))