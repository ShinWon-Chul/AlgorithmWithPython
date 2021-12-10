import heapq
inf = int(1e9)
v, e = list(map(int, input().rstrip().split()))
start = int(input())
distance = [inf] * (v+1)
distance[start] = 0

graph = [[] for _ in range(v+1)]
for _ in range(e):
    sn, en, d = list(map(int, input().rstrip().split()))
    graph[sn].append((d,en))

h = []

def Dijcstra():
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
                
Dijcstra()
for i in range(1, v+1):
    if distance[i] == inf:
        print("INF")
    else:    
        print(distance[i])