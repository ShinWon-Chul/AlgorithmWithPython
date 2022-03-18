import heapq
from collections import Counter

def solution(n, edge):
    inf = int(1e9)
    start = 1
    distance = [inf] * (n+1)
    distance[start] = 0

    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append((1,e))
        graph[e].append((1,s))

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
    distance = distance[1:]
    max_distance = max(distance)
    return Counter(distance)[max_distance]