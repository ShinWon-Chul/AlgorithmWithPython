import heapq

def Dijcstra(start, graph, distance):
    h = []
    heapq.heappush(h, (0, start))
    while h:
        dist, current = heapq.heappop(h)
        if distance[current] < dist:
            continue
        for i in graph[current]:
            new_dist = dist + i[0]
            if new_dist < distance[i[1]]:
                distance[i[1]] = new_dist
                heapq.heappush(h, (new_dist, i[1]))
    return distance

def solution(N, road, K):
    answer = 0
    inf = int(1e9)
    distance = [inf for _ in range(N+1)]
    distance[1] = 0
    
    graph = [[] for _ in range(N+1)]
    for a, b, dist in road:
        graph[a].append([dist, b])
        graph[b].append([dist, a])
    distance = Dijcstra(1, graph, distance)
    
    for dist in distance:
        if dist <= K:
            answer += 1
    return answer